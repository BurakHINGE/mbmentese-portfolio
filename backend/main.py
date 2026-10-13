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
    # Düşük temperature modelin Türkçe uydurma/çarpık kelimeler üretmesini engeller
    chat_client.settings.temperature = 0.1
    chat_client.settings.top_p = 0.9
    chat_client.settings.presence_penalty = 0.3
    print("✅ Model başarıyla yüklendi! API istekleri dinlemeye hazır.")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Local RAG Assistant API calisiyor!"}

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    global chat_client
    user_query = request.message.strip()
    
    if not user_query:
        raise HTTPException(status_code=400, detail="Mesaj boş olamaz.")
        
    print(f"\n📩 Gelen Soru: {user_query}")
    
    # 1. RAG: Veritabanından alakalı paragrafları bul ve mükerrer parçaları temizle
    top_chunks = get_top_chunks(user_query, top_k=3)
    seen_chunks = set()
    unique_texts = []
    for score, text in top_chunks:
        cleaned = text.strip()
        if cleaned not in seen_chunks:
            seen_chunks.add(cleaned)
            unique_texts.append(cleaned)
            
    context = "\n\n".join(unique_texts)
        
    # 2. Sistem Prompt'u
    system_prompt = f"""Sen Mehmet Burak Menteşe'nin kişisel portfolyo web sitesindeki resmi yapay zeka asistanısın.
Ziyaretçilere Mehmet Burak Menteşe'nin projeleri, blog yazıları, teknik yetenekleri ve sitedeki terimler hakkında bilgi vermekle görevlisin.

KESİN KURALLAR:
1. ASLA TEKRARA DÜŞME: Bir bilgi (örneğin LinkedIn veya GitHub bağlantısı, okul adı veya bir özellik) BİLGİLER kısmında birden fazla kez yer alsa dahi, cevabında onu YALNIZCA BİR KEZ belirt. Aynı cümleyi, bağlantıyı veya ifadeyi iki kez art arda tekrarlama.
2. DİL VE DÜZGÜN TÜRKÇE: Uydurma, yapay, bozuk veya çarpıtılmış kelimeler kullanma. Dil bilgisi kurallarına tam uyarak, sade, anlaşılır, net ve temiz bir Türkçe ile cevap ver. Cümleleri gereksiz yere uzatma.
3. KANITA DAYALI CEVAP VER: Yalnızca aşağıdaki 'BİLGİLER' bölümündeki gerçek detaylara dayanarak cevap ver. Eğer kullanıcının sorduğu detay metinde açıkça yoksa, bilgi uydurmak yerine kesinlikle "Bu konuda veritabanımda bir bilgi bulunmuyor." de.
4. DOĞRUDAN YANIT: Düşünce sürecini veya 'Kibarca:' gibi ifadeleri yazma; doğrudan sorunun cevabını ver.

BİLGİLER:
{context}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
    
    try:
        response = chat_client.complete_chat(messages)
        if hasattr(response, 'choices') and len(response.choices) > 0:
            answer = response.choices[0].message.content.strip()
        else:
            answer = str(response)
            
        print(f"🤖 Cevap: {answer}\n")
        return {"response": answer}
    except Exception as e:
        print(f"Hata: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
