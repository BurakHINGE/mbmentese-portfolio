## Local RAG Asistanı (Bölüm 2) Blog Yazısı Genel Bakış ve Kapsamı
Soru: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 2 / Part 2) blog yazısı neyi anlatıyor, ne zaman yayımlandı ve kapsamı nedir?
Cevap: Mehmet Burak Menteşe'nin 19 Temmuz 2026 tarihinde kaleme aldığı **"Local RAG Asistanı Geliştirmek: Microsoft Foundry ile Bölüm 2"** (Medium başlığıyla **"Local RAG Asistanı Geliştirmek: Chunking, Kosinüs Benzerliği ve Sohbet (Bölüm 2)"**, İngilizce: **"Developing a Local RAG Assistant: Part 2 with Microsoft Foundry"**, sitedeki kart adıyla **Local RAG Asistanı (Bölüm 2)** / **Local RAG Assistant (Part 2)**, bağlantı: `https://mburakmentese.dev/blog/local-RAG-bolum-2`) başlıklı makale, projenin 2. fazını (**Phase 2: Data Ingestion & Retrieval**) ele alır.
5 dakikalık okuma süresine sahip olan bu teknik rehber (Etiketler: `Chunking`, `Retrieval`, `Python`, `Cosine Similarity`, `Vector DB`, `Search Engine`); uzun dokümanların anlamlı parçalara bölünmesi (**Chunking**), kosinüs benzerliği (**Cosine Similarity**) ile anlamsal arama motoru geliştirilmesi ve terminal üzerinden canlı **CLI** sohbet döngüsünün kurulması süreçlerini adım adım anlatır.

## Local RAG Bölüm 2 (Phase 2): Koca Bir Dosyayı Yapay Zekaya Neden Doğrudan Veremeyiz? (Context Window ve Lost in the Middle)
Soru: Local RAG sisteminde büyük bir dokümanı veya PDF'i neden tek seferde prompt olarak modele veremeyiz? Context Window ve Lost in the Middle problemi nedir?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 2 / Phase 2) blog yazısında açıklandığı üzere, devasa bir belgeyi tek seferde dil modeline vermememizin 3 temel mühendislik nedeni vardır:
1. **Context Window (Bağlam Penceresi Sınırı):** Yapay zeka modellerinin tek seferde okuyup işleyebileceği "Context Window" adı verilen kısa süreli bir hafıza (token) sınırı vardır; çok uzun metinler bu sınıra takılıp hata verir.
2. **Lost in the Middle (Ortada Kaybolma Problemi):** Modele çok uzun bir metin tek seferde verildiğinde, model metnin başını unutup yalnızca sonunu hatırlama veya ortadaki kritik bilgileri gözden kaçırma eğilimi gösterir; buna literatürde **"Lost in the Middle"** problemi denir.
3. **Performans ve Donanım Yükü:** Her soruda yüzlerce sayfalık metni baştan aşağı okutmak yerel cihazı (özellikle çevrimdışı CPU/NPU ortamında) aşırı yorar ve yanıt süresini saniyelerden dakikalara çıkarır. Bu nedenle tüm dosyayı değil, yalnızca sorulan soruyla en alakalı küçük paragrafı (chunk) bulup modele kopya kağıdı olarak vermek gerekir.

## Local RAG Bölüm 2 (1. Adım): Chunking (Veriyi Parçalama) Mantığı, `ingest.py` ve `chunk_text()` Fonksiyonu
Soru: Local RAG (Bölüm 2) projesinde Data Ingestion ve Chunking (metin parçalama) işlemi nasıl kodlandı, `ingest.py` ve `chunk_text()` fonksiyonu nasıl çalışır?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 2 / Phase 2) yazısının 1. adımında anlatıldığı üzere; projede bir **`docs`** klasörü oluşturularak içerisine uzun dokümanlar ("Siber Güvenlik Kulübü Notları" vb.) yerleştirilmiştir. Veri işleme (**Data Ingestion**) sürecini yürüten **`ingest.py`** betiğindeki **`chunk_text(text)`** fonksiyonu şu adımlarla çalışır:
- Metni çift satır sonu karakterine (`\n\n` — paragraf boşluklarına, `text.split('\n\n')`) göre bölerek anlamlı paragraflara ayırır.
- 10 karakterden daha kısa olan (`len(p.strip()) > 10`) boş veya anlamsız satır parçalarını filtreleyerek temizler.
- Elde edilen her bir anlamlı paragrafı Microsoft Foundry Local üzerindeki **`qwen3-embedding-0.6b`** modeline göndererek **1024 boyutlu** vektörlere dönüştürür ve yerel **SQLite (`knowledge_base.db`)** veritabanına yığınlar (**batch**) halinde kaydeder.

## Local RAG Bölüm 2 (2. Adım): Kosinüs Benzerliği (Cosine Similarity) ile Arama Motoru ve `retrieve.py`
Soru: Local RAG (Bölüm 2) sisteminde Kosinüs Benzerliği (Cosine Similarity) nedir, `retrieve.py` arama motoru doğru paragrafı nasıl bulur?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 2 / Phase 2) yazısının 2. adımında açıklandığı üzere; kullanıcı bir soru sorduğunda arama motoru (**`retrieve.py`**) önce kullanıcının sorusunu da `qwen3-embedding-0.6b` ile **1024 boyutlu** bir vektöre çevirir. Ardından soru vektörü ile SQLite veritabanındaki her bir paragrafın vektörü arasındaki açının kosinüsünü (**Cosine Similarity / Kosinüs Benzerliği**) matematiksel olarak hesaplar.
- **Çalışma Prensibi ve Test Sonucu:** İki vektör arasındaki geometrik açı ne kadar darsa ve kosinüs benzerlik skoru **1.0**'a ne kadar yakınsa, iki metin anlamca o kadar birbiriyle örtüşüyor demektir. Mehmet Burak Menteşe'nin `retrieve.py` ile yaptığı testlerde, *"Eğitimler nerede yapılıyor?"* sorusuna karşılık gelen *"Salı ve Perşembe günleri Mühendislik Fakültesi laboratuvarlarında yapılmaktadır"* cümlesi **0.6261** gibi yüksek bir benzerlik skoruyla saniyeler içinde en tepeye çıkarılarak başarıyla bulunmuştur.

## Local RAG Bölüm 2 (3. Adım): Tüm Bileşenlerin Birleştirilmesi ve `app.py` ile CLI Sohbet Döngüsü
Soru: Local RAG (Bölüm 2) projesinde `app.py` dosyası ne işe yarar, bileşenler nasıl birleştirildi ve terminalden (CLI) canlı sohbet nasıl sağlandı?
Cevap: Mehmet Burak Menteşe, Local RAG Asistanı (Bölüm 2 / Phase 2) yazısının 3. adımında **`app.py`** dosyasını oluşturarak iki ana yapay zeka bileşenini tek bir çatı altında birleştirmiştir:
1. Soruya en uygun metin parçasını saniyeler içinde bulan anlamsal arama motoru (**`qwen3-embedding-0.6b`** + SQLite Kosinüs Benzerliği).
2. Yalnızca kendisine verilen bağlam metnine bakarak cevap üreten yerel sohbet modeli (**`phi-3.5-mini`** SLM).
`app.py` içinde sürekli çalışan interaktif bir **CLI (komut satırı / terminal)** sohbet döngüsü kurulmuştur. Kullanıcı terminalden sorusunu yazdığında arama motoru SQLite'tan en alakalı not parçasını çeker, bu notu katı İngilizce sistem promptunun (`Context`) içine yerleştirir ve `phi-3.5-mini` modeline sunar; model de halüsinasyon görmeden doğrudan Türkçe ve net bir yanıt üretir.

## Local RAG Bölüm 2 (Phase 2) Sonucu ve 3. Bölümde (Phase 3) Neler Yapılacak?
Soru: Mehmet Burak Menteşe'nin Local RAG blog serisinin 2. bölümünün (Phase 2) sonunda ne elde edildi ve 3. bölümde (Phase 3) neler anlatılıyor?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı blog serisinin 2. bölümünün (**Phase 2**) sonunda; hiçbir bulut servisine veri göndermeden, tamamen yerel CPU donanımıyla çalışan, `docs` klasöründeki kişisel notları okuyup hızlı ve kararlı cevaplar veren uçtan uca çalışan çevrimdışı (offline) bir yapay zeka asistanı elde edilmiştir. Serinin **3. ve final bölümünde (Phase 3)** ise asistanın uç senaryolarla (boş girdiler, halüsinasyon tuzakları) test edilmesi, Apple Silicon (MacBook) üzerinde hız ve performans optimizasyonları ve projenin açık kaynak olarak yayınlanması ele alınmaktadır.
