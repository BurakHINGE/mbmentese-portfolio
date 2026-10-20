from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from foundry_local_sdk import Configuration, FoundryLocalManager
from retrieve import get_top_chunks
import uvicorn

app = FastAPI(title="Local RAG Assistant API")

# Sitenin API'ye rahatça istek atabilmesi için CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında her yerden erişime izin verir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global model ve client değişkenleri
chat_client = None

@app.on_event("startup")
def startup_event():
    global chat_client
    print("🚀 Foundry Local ve Phi-3.5 modeli yükleniyor...")
    
    config = Configuration(app_name="LocalRAGAssistant")
    try:
        FoundryLocalManager.initialize(config)
    except Exception:
        pass  # Zaten initialize edildiyse hata vermemesi için
        
    manager = FoundryLocalManager.instance
    model = manager.catalog.get_model_variant("Phi-3.5-mini-instruct-generic-cpu:2")
    
    if model is None:
        raise RuntimeError("Phi-3.5 modeli bulunamadı!")
        
    model.load()
    chat_client = model.get_chat_client()
    chat_client.settings.temperature = 0.1
    chat_client.settings.top_p = 0.9
    print("✅ Model başarıyla yüklendi! API istekleri dinlemeye hazır.")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Local RAG Assistant API calisiyor!"}

import re

GREETINGS = {
    "selam", "merhaba", "selamlar", "merhabalar", "hey", "hi", "hello",
    "gunaydin", "günaydın", "iyi gunler", "iyi günler", "iyi aksamlar",
    "iyi akşamlar", "naber", "nasılsın", "nasilsin", "slm", "mrb"
}

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    global chat_client
    user_query = request.message.strip()
    
    if not user_query:
        raise HTTPException(status_code=400, detail="Mesaj boş olamaz.")
        
    print(f"\n📩 Gelen Soru: {user_query}")
    
    # 1. Selamlaşma / Hatır sorma yakalayıcı (Modeli ve veritabanını boşuna yormadan anında doğal Türkçe cevap)
    clean_query = re.sub(r'[^\w\s]', '', user_query.lower()).strip()
    if clean_query in GREETINGS:
        greeting_reply = "Merhaba! Ben Mehmet Burak Menteşe'nin portfolyo yapay zeka asistanıyım. Projeler, blog yazıları, teknik yetenekler veya eğitim geçmişi hakkında sorularınızı yanıtlayabilirim. Size nasıl yardımcı olabilirim? 😊"
        print(f"🤖 Cevap: {greeting_reply}\n")
        return {"response": greeting_reply}
    
    # 2. RAG: Veritabanından alakalı paragrafları bul
    top_chunks = get_top_chunks(user_query, top_k=5)
    
    for idx, (score, txt) in enumerate(top_chunks):
        print(f"  [Chunk {idx+1}] Skor: {score:.4f} | Başlık: {txt[:80]}...")

    # Eşik Değeri (Threshold): Eğer bulunan en iyi belgenin benzerliği 0.35'in altındaysa veritabanında bu bilgi kesinlikle yoktur!
    if not top_chunks or top_chunks[0][0] < 0.35:
        no_info_reply = "Bu konuda veritabanımda bir bilgi bulunmuyor. Mehmet Burak Menteşe'nin projeleri, eğitim geçmişi, teknik yetenekleri veya blog yazıları hakkında sorular sorabilirsiniz."
        print(f"🤖 Cevap (Düşük benzerlik skoru {top_chunks[0][0] if top_chunks else 0:.3f}): {no_info_reply}\n")
        return {"response": no_info_reply}
        
    best_score = top_chunks[0][0]
    # Sadece en iyi sonuca yakın ve alaka düzeyi yüksek parçaları seç (çapraz doküman kirliliğini engeller)
    relevant_chunks = [c for c in top_chunks if c[0] >= 0.38 and (best_score - c[0]) <= 0.15]
    if not relevant_chunks:
        relevant_chunks = [top_chunks[0]]

    # Mükerrer parçaları temizle
    seen_chunks = set()
    unique_texts = []
    for score, text in relevant_chunks:
        cleaned = text.strip()
        if cleaned not in seen_chunks:
            seen_chunks.add(cleaned)
            unique_texts.append(cleaned)
            
    context = "\n\n".join(unique_texts)
        
    # 3. Prompt Yapısı
    user_prompt = f"""You are the official AI assistant for Mehmet Burak Menteşe's personal portfolio.

Context:
{context}

Question: {user_query}

Instructions:
1. Answer the question directly, politely, and factually in fluent Turkish using ONLY the facts provided in the Context above.
2. If the Context does not contain the factual answer to the Question, reply ONLY:
Bu konuda veritabanımda bir bilgi bulunmuyor.
3. Keep the answer concise, direct, and to the point.
4. Provide links, emails, and factual information directly without describing website UI layouts.
5. Do not mention other unrelated facts, do not hallucinate, and do not include disclaimers or notes."""

    messages = [
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = chat_client.complete_chat(messages)
        if hasattr(response, 'choices') and len(response.choices) > 0:
            answer = response.choices[0].message.content.strip()
        else:
            answer = str(response)

        raw_model_output = answer
        print(f"--- RAW MODEL OUTPUT ---\n{answer}\n------------------------")

        # 1. Modelin ürettiği olası ret meta-yorumlarını temizle
        refusal_phrases = [
            "Bu konuda veritabanımda bir bilgi bulunmuyor",
            "Bu konuda veritabanımda bilgi bulunmuyor",
            "Bu konuda veritabanında bilgi bulunmuyor",
            "bu konuda veritabanımda bir bilgi bulunmuyor",
            "bu konuda veritabanımda bilgi bulunmuyor",
            "veritabanımda bir bilgi bulunmuyor",
            "veritabanımda bilgi bulunmuyor"
        ]
        
        # Eğer cevap tek başına bir ret cümlesi ise standart formata dönüştür
        if any(answer.strip().lower().startswith(r.lower()) for r in refusal_phrases):
            answer = "Bu konuda veritabanımda bir bilgi bulunmuyor."
        else:
            # Trailing ret veya meta-yorum paragraflarını temizle
            if "\n\n" in answer:
                parts = answer.split("\n\n")
                cleaned_parts = [parts[0]]
                for part in parts[1:]:
                    p_lower = part.strip().lower()
                    if any(p_lower.startswith(prefix) for prefix in [
                        "bu konu", "bu soru", "bu bilgi", "veritabanı", "özür", "(not", "note:", "not:", "i do not"
                    ]):
                        break
                    cleaned_parts.append(part)
                answer = "\n\n".join(cleaned_parts).strip()

            for delimiter in refusal_phrases + [
                "(Veritabanımda bilgi bulunmuyor",
                "(veritabanımda bilgi bulunmuyor",
                "\n\nÖzür dilerim", "\nÖzür dilerim",
                "\n\nAlternatif", "\nAlternatif", 
                "\n\n(Not:", "\n(Not:", "(Not:",
                "\n\nNote:", "\nNote:", "(Note:"
            ]:
                if delimiter.lower() in answer.lower() and not answer.strip().lower().startswith(delimiter.lower()):
                    idx = answer.lower().find(delimiter.lower())
                    if idx > 0:
                        answer = answer[:idx].strip()

        # 2. Eğer temizlendikten sonra boş kaldıysa standart mesaja dönüştür
        # Trailing tek harf veya yarım kalan satır temizliği (örn: \n\nB)
        answer = re.sub(r'\n+[A-Za-zÇĞİÖŞÜçğıöşü\s]{1,3}$', '', answer).strip()

        if not answer:
            answer = "Bu konuda veritabanımda bir bilgi bulunmuyor."

        print(f"🤖 Cevap: {answer}\n")
        return {"response": answer}
    except Exception as e:
        print(f"Hata: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
