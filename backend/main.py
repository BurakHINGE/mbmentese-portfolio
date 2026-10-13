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
    top_chunks = get_top_chunks(user_query, top_k=3)
    
    for idx, (score, txt) in enumerate(top_chunks):
        print(f"  [Chunk {idx+1}] Skor: {score:.4f} | Başlık: {txt[:80]}...")

    # Eşik Değeri (Threshold): Eğer bulunan en iyi belgenin benzerliği 0.35'in altındaysa veritabanında bu bilgi kesinlikle yoktur!
    if not top_chunks or top_chunks[0][0] < 0.35:
        no_info_reply = "Bu konuda veritabanımda bir bilgi bulunmuyor. Mehmet Burak Menteşe'nin projeleri, eğitim geçmişi, teknik yetenekleri veya blog yazıları hakkında sorular sorabilirsiniz."
        print(f"🤖 Cevap (Düşük benzerlik skoru {top_chunks[0][0] if top_chunks else 0:.3f}): {no_info_reply}\n")
        return {"response": no_info_reply}
        
    # Mükerrer parçaları temizle
    seen_chunks = set()
    unique_texts = []
    for score, text in top_chunks:
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
- If the Context does not contain the factual answer to the Question, your entire response must be simply: "Bu konuda veritabanımda bir bilgi bulunmuyor."
- If the Context contains the answer, answer warmly, politely, and factually in fluent Turkish.
- Keep the answer concise, direct, and to the point. Stop generating once the question is answered.
- Provide links, emails, and factual information directly without describing website UI layouts.
- Do not mention other unrelated facts, do not hallucinate, and do not include disclaimers or notes."""

    messages = [
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = chat_client.complete_chat(messages)
        if hasattr(response, 'choices') and len(response.choices) > 0:
            answer = response.choices[0].message.content.strip()
        else:
            answer = str(response)

        print(f"--- RAW MODEL OUTPUT ---\n{answer}\n------------------------")

        raw_debug = answer
        # 1. Modelin ürettiği olası kuyruk meta-yorumları, özür/not bloklarını temizle
        for delimiter in [
            "\n\nÖzür dilerim", "\nÖzür dilerim",
            "\n\nBu konuda veritabanımda", "\nBu konuda veritabanımda",
            "\n\nAlternatif", "\nAlternatif", 
            "\n\n(Not:", "\n(Not:", "(Not:",
            "\n\nNote:", "\nNote:", "(Note:"
        ]:
            if delimiter in answer:
                answer = answer.split(delimiter)[0].strip()

        # 2. Eğer temizlendikten sonra kalan metin "bilgi bulunmuyor" diyorsa veya boşsa standart mesaja dönüştür
        lower_ans = answer.lower()
        if not answer or lower_ans.startswith("bu konuda veritabanımda") or "bilgi yer almıyor" in lower_ans:
            answer = "Bu konuda veritabanımda bir bilgi bulunmuyor."

        print(f"🤖 Cevap: {answer}\n")
        return {"response": answer}
    except Exception as e:
        print(f"Hata: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
