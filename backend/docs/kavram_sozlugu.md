## RAG (Retrieval-Augmented Generation / Erişim Destekli Üretim) Nedir?
Soru: RAG (Retrieval-Augmented Generation) nedir, nasıl çalışır ve Mehmet Burak Menteşe'nin projelerinde nasıl kullanılmıştır?
Cevap: RAG (Retrieval-Augmented Generation), yapay zeka dil modellerinin (LLM / SLM) kendi eğitim verileri dışındaki özel ve güvenilir belgelere dayanarak doğru cevaplar üretmesini sağlayan gelişmiş bir mimaridir. Model doğrudan ezberinden cevap üretmek yerine 3 adımda çalışır: Önce kullanıcının veritabanında anlamsal (semantik) arama yaparak soruyla ilgili bilgi parçalarını bulup getirir (Retrieve), bu bilgileri sistem yönergesi (prompt) ile birleştirir (Augment) ve son olarak yalnızca bu kanıtlara dayanarak halüsinasyon görmeden doğru cevabı üretir (Generate). Mehmet Burak Menteşe, hem Microsoft AI Innovators stajındaki Yerel RAG Asistanı projesini hem de şu an mburakmentese.dev portfolyo sitesinde çalışan yapay zeka asistanını sıfırdan RAG mimarisiyle geliştirmiştir.

## Clean URL (Temiz Bağlantı Yapısı) Nedir?
Soru: Clean URL nedir, ne işe yarar ve mburakmentese.dev sitesinde nasıl kullanılmıştır?
Cevap: Clean URL, web sitelerindeki sayfa adreslerinin sonunda bulunan '.html', '.php' gibi dosya uzantılarının ve karmaşık sorgu parametrelerinin kaldırılarak 'mburakmentese.dev/hakkimda' veya 'mburakmentese.dev/projeler' gibi çok daha temiz, okunaklı, güvenli ve modern bir şekilde gösterilmesidir. Ziyaretçi deneyimini, güvenliği ve arama motoru optimizasyonunu (SEO) artırır. Mehmet Burak Menteşe'nin kişisel portfolyo web sitesinde (mburakmentese.dev) Cloudflare CDN üzerinden Clean URL yapısı kullanılmaktadır.

## Vanilla JavaScript, Vanilla CSS ve Vanilla HTML Nedir?
Soru: Vanilla JS (Vanilla JavaScript) ve Vanilla CSS nedir, neden framework yerine tercih edilir?
Cevap: Vanilla JavaScript ve Vanilla CSS; React, Angular, Vue veya Tailwind, Bootstrap gibi harici hiçbir kütüphane ya da framework kullanmadan, doğrudan web tarayıcısının sunduğu saf, yerel ve yalın web standartlarıyla yazılım geliştirilmesi anlamına gelir. Harici paket yükü olmadığı için çok yüksek açılış hızı ve tam kontrol sağlar. Mehmet Burak Menteşe'nin hem kendi portfolyo web sitesi (mburakmentese.dev) hem de geliştirdiği Marmara Siber Web Arayüzü (marmaracyber.com) tamamen sıfırdan Vanilla HTML5, CSS3 ve JavaScript teknolojileriyle inşa edilmiştir.

## Yapay Zekada Halüsinasyon (Hallucination / Uydurma) Nedir?
Soru: Yapay zekada halüsinasyon (hallucination) nedir ve Mehmet Burak Menteşe bu sorunu nasıl çözmüştür?
Cevap: Halüsinasyon (Hallucination), bir yapay zeka dil modelinin cevabını bilmediği veya eğitim verisinde/veritabanında yer almayan bir soruya, sanki gerçekmiş gibi kendinden emin bir şekilde uydurma, yanlış ve tutarsız cevaplar üretmesi durumudur. Mehmet Burak Menteşe, geliştirdiği Yerel RAG Asistanı projesinde modelleri SQLite üzerindeki gerçek belgelere bağlayarak ve katı İngilizce sistem promptları (Prompt Engineering) kullanarak halüsinasyonu sıfıra indirmiştir.

## i18n (Internationalization / Uluslararasılaşma ve Çift Dilli Çeviri Motoru) Nedir?
Soru: i18n (Internationalization) nedir ve Mehmet Burak Menteşe'nin web sitelerinde nasıl çalışır?
Cevap: i18n (kelimenin başındaki 'i' ve sonundaki 'n' harfleri arasındaki 18 harften adını alan Internationalization kavramı), web sitelerinin veya yazılımların farklı dillere kolayca uyarlanabilmesini sağlayan çoklu dil mimarisidir. Mehmet Burak Menteşe'nin hem kişisel portfolyo sitesinde (mburakmentese.dev) hem de Marmara Siber web sitesinde (marmaracyber.com), sayfayı yeniden yüklemeye gerek kalmadan Türkçe (TR) ve İngilizce (EN) dilleri arasında anında geçiş yapan özel bir Vanilla JavaScript i18n çeviri motoru bulunmaktadır.

## JavaFX Nedir?
Soru: JavaFX nedir ve Mehmet Burak Menteşe hangi projelerinde JavaFX kullanmıştır?
Cevap: JavaFX, Java programlama dili ile modern, zengin, interaktif ve grafiksel kullanıcı arayüzüne (GUI) sahip masaüstü uygulamaları ve 2D oyunlar geliştirmek için kullanılan güçlü bir grafik ve medya kütüphanesidir. Mehmet Burak Menteşe, konsoldan masaüstü arayüzüne taşıdığı Library Management System (Kütüphane Yönetim Sistemi) projesinde ve hiçbir hazır oyun motoru kullanmadan sıfırdan geliştirdiği GhostHunterINC (GhostHunterGame) 2D oyun projesinde arayüz ve sahne teknolojisi olarak JavaFX kullanmıştır.

## JSON Kalıcılığı (JSON Persistence) Nedir?
Soru: JSON Kalıcılığı (JSON Persistence) nedir ve Kütüphane Yönetim Sistemi projesinde nasıl kullanılmıştır?
Cevap: JSON Kalıcılığı (JSON Persistence), bir yazılımdaki çalışma zamanı verilerinin (örneğin kullanıcı hesapları, roller ve kitap kayıtları) program kapatıldığında veya bilgisayar yeniden başlatıldığında kaybolmaması için, harici bir SQL veritabanı sunucusu kurulumuna ihtiyaç duymadan yerel JSON dosyalarında (serialization/deserialization ile) güvenle saklanması işlemidir. Mehmet Burak Menteşe, Library Management System projesinde tüm kullanıcı ve envanter verilerini 'users.json' ve 'libraryBooks.json' dosyaları üzerinden kalıcı hale getirmiştir.

## Kosinüs Benzerliği (Cosine Similarity) Nedir?
Soru: Kosinüs Benzerliği (Cosine Similarity) nedir ve Local RAG Asistanı projesinde nasıl çalışır?
Cevap: Kosinüs Benzerliği (Cosine Similarity), çok boyutlu uzaydaki iki sayısal vektör arasındaki açının kosinüsünü hesaplayarak iki metnin anlamsal olarak birbirine ne kadar benzediğini ölçen matematiksel bir yöntemdir. Skor 1.0'a ne kadar yakınsa metinler anlamca o kadar birbiriyle örtüşür. Mehmet Burak Menteşe'nin geliştirdiği Yerel RAG Asistanı projesinde (retrieve.py), kullanıcının sorusunun 1024 boyutlu vektörü ile SQLite veritabanındaki belge parçalarının vektörleri karşılaştırılarak en alakalı 4 parçanın (Top-4 chunk) saniyeler içinde bulunması için Kosinüs Benzerliği kullanılmıştır.

## Agentic AI (Ajan Tabanlı Yapay Zeka) ve Google ADK Nedir?
Soru: Agentic AI (Ajan Tabanlı Yapay Zeka) ve Google ADK (Agent Development Kit) nedir?
Cevap: Agentic AI, yalnızca tek seferlik metin yanıtları üretmekle kalmayıp, kendisine verilen karmaşık bir hedefe ulaşmak için bağımsız olarak alt adımları planlayan, harici araçları (API, veritabanı, terminal, arama motoru) otonom olarak kullanan ve sonuçları değerlendirip kendi kendini düzeltebilen yapay zeka ajanları mimarisidir. Google ADK (Agent Development Kit) ise Google tarafından bu otonom yapay zeka ajanlarını geliştirmek için sunulan yazılım geliştirme kitidir. Mehmet Burak Menteşe, MultiGroup Community tarafından düzenlenen 6 modüllü 'Agentic AI Development with Google ADK & MCP' eğitimini ve KOMTAŞ AI Explorer Bootcamp'26 programını tamamlayarak bu alanda çalışmalar gerçekleştirmiştir.

## MCP (Model Context Protocol) Nedir?
Soru: MCP (Model Context Protocol) nedir ve yapay zeka sistemlerinde ne işe yarar?
Cevap: MCP (Model Context Protocol), yapay zeka dil modelleri ile geliştirici ortamları, yerel dosyalar, veritabanları veya harici kurumsal araçlar arasında güvenli, standart ve çift yönlü bir iletişim sağlayan açık kaynaklı bir protokoldür. Yapay zeka ajanlarının dış dünyadaki veri kaynaklarına ve geliştirme araçlarına tek bir standart üzerinden bağlanmasını sağlar. Mehmet Burak Menteşe, MultiGroup Community bünyesindeki 'Agentic AI Development with Google ADK & MCP' eğitim serisinde MCP standardı üzerine uzmanlaşmıştır.

## MAC Adresi, ARP Protokolü ve ARP Spoofing (ARP Zehirlenmesi) Nedir?
Soru: MAC adresi, ARP protokolü ve ARP Spoofing (ARP Zehirlenmesi) nedir?
Cevap: MAC adresi (Media Access Control), bir cihazın ağ kartına (NIC) üretim aşamasında kalıcı olarak atanmış 48 bitlik (12 onaltılık/hexadecimal karakterli, örn: A4:BC:12:DE:34:56) fiziksel donanım kimliğidir ve OSI modelinin 2. katmanında (Data Link) çalışır. ARP (Address Resolution Protocol) ise yerel ağda (LAN) bilinen bir IPv4 adresini fiziksel MAC adresine çeviren köprü protokolüdür (IPv6'da bu görevi NDP üstlenir). ARP Spoofing (ARP Zehirlenmesi), bir saldırganın yerel ağdaki cihazlara sahte ARP yanıtları göndererek ağ trafiğini kendi üzerine çekmesi ve araya girmesi (Man-in-the-Middle / MITM) saldırısıdır. Mehmet Burak Menteşe bu konuyu 'MAC Adresi ve ARP: Cihazlar Nasıl İletişim Kurar?' başlıklı blog yazısında detaylıca anlatmış ve SyberTÜRK stajında Wireshark/Bettercap araçlarıyla pratik olarak incelemiştir.

## Kuantum Bilişim (Quantum Computing), Kübit (Qubit) ve Süperpozisyon Nedir?
Soru: Kuantum bilişim, kübit (qubit) ve süperpozisyon nedir, Mehmet Burak Menteşe'nin bu alandaki sertifikaları nelerdir?
Cevap: Kuantum bilişim, klasik bilgisayarların kullandığı ikili bitler (yalnızca 0 veya 1) yerine kuantum mekaniği ilkelerinden yararlanan kübitler (qubits) ile çalışan ileri hesaplama alanıdır. Süperpozisyon (Superposition) ilkesi sayesinde bir kübit aynı anda hem 0 hem 1 durumunun doğrusal bir kombinasyonunda bulunabilir; bu da klasik bilgisayarların çözmekte zorlandığı karmaşık matematiksel ve kriptografik problemlerin çok daha hızlı modellenmesini sağlar. Mehmet Burak Menteşe, QWorld tarafından düzenlenen eğitimleri tamamlayarak QPrep (kuantum için lineer cebir altyapısı) ve QBronze (kübit, süperpozisyon ve temel kuantum algoritmaları) sertifikalarını almıştır.

## Agile ve Scrum Sprint Metodolojisi Nedir?
Soru: Agile (Çevik) yazılım geliştirme ve Scrum sprint metodolojisi nedir?
Cevap: Agile (Çevik metodoloji), yazılım projelerinde katı ve değişmez planlar yerine hızlı adaptasyon, ekip içi sürekli iletişim ve aşamalı gelişim sağlayan modern bir yazılım geliştirme felsefesidir. Scrum sprintleri ise projenin genellikle 1 ila 2 haftalık kısa döngülere (sprint) bölünerek her hafta belirli görevlerin planlanıp tamamlandığı ve gözden geçirildiği çalışma düzenidir. Mehmet Burak Menteşe, Marmara Üniversitesi Sosyal Teknoloji Kulübü'ndeki 15-20 kişilik Unity oyun geliştirme ekibinde ve diğer grup projelerinde haftalık Agile/Scrum sprintlerini ve Git/GitHub iş birliği süreçlerini aktif olarak yürütmüştür.

## Chunking (Belge ve Metin Parçalama) Nedir?
Soru: Chunking (metin parçalama) nedir ve Local RAG projesinde nasıl uygulanmıştır?
Cevap: Chunking, büyük belgelerin veya uzun metinlerin (PDF, Markdown, makale vb.) yapay zeka modellerinin bağlam penceresine (context window) sığabilmesi ve anlamsal odaklanmanın kaybolmaması amacıyla mantıksal ve yönetilebilir küçük paragraflara bölünmesi işlemidir. Mehmet Burak Menteşe'nin geliştirdiği Yerel RAG Asistanı projesinde 'ingest.py' içindeki 'chunk_text()' fonksiyonu, belgeleri çift satır sonlarına göre anlamlı paragraflara ayırarak ve 10 karakterden kısa anlamsız parçaları filtreleyerek yüksek doğruluklu vektör aramasına hazırlar.

## Embedding (Vektörleştirme / Vektör Gömme) ve `qwen3-embedding-0.6b` Nedir?
Soru: Embedding (vektörleştirme) ve `qwen3-embedding-0.6b` modeli nedir, kaç boyutlu vektör üretir?
Cevap: Embedding (Vektörleştirme), metinlerin, kelimelerin ve cümlelerin anlamsal ilişkilerini koruyacak şekilde çok boyutlu sayısal vektör dizilerine (koordinatlara) dönüştürülmesidir; bu sayede bilgisayar kelimelerin yalnızca harf yazılışına değil, anlam yakınlığına bakar. 'qwen3-embedding-0.6b', Mehmet Burak Menteşe'nin Yerel RAG Asistanı projesinde Microsoft Foundry Local üzerinden kullandığı, cümleleri minimum CPU yüküyle tam 1024 boyutlu yüksek doğruluklu sayısal vektörlere dönüştüren hafif ve optimize bir embedding modelidir.

## Microsoft Foundry Local SDK Nedir?
Soru: Microsoft Foundry Local SDK nedir ve Mehmet Burak Menteşe'nin Local RAG projesinde ne işe yarar?
Cevap: Microsoft Foundry Local SDK, büyük/küçük dil modellerini (LLM/SLM) ve embedding modellerini harici bulut sunucularına, internet bağlantısına veya ücretli API anahtarlarına ihtiyaç duymadan, doğrudan kullanıcının kendi yerel bilgisayarında (CPU, NPU veya Apple Silicon donanımında) çevrimdışı (offline) olarak çalıştırmayı ve yönetmeyi sağlayan yerel yapay zeka çalışma ortamıdır. Mehmet Burak Menteşe, Microsoft AI Innovators yaz stajında geliştirdiği Yerel RAG Asistanı projesinde 'qwen3-embedding-0.6b' ve 'phi-3.5-mini' modellerini yerel CPU üzerinde çalıştırmak için Microsoft Foundry Local SDK kullanmıştır.

## Phi-3.5-mini Dil Modeli ve SLM (Small Language Model) Nedir?
Soru: Phi-3.5-mini modeli ve SLM (Small Language Model / Küçük Dil Modeli) nedir, LLM ile farkı nedir?
Cevap: SLM (Small Language Model / Küçük Dil Modeli), yüz milyarlarca parametreli devasa LLM'lerin (Büyük Dil Modelleri) aksine, daha az parametreye sahip olan ve kişisel bilgisayarlarda pahalı ekran kartları (GPU) gerektirmeden yerel CPU/NPU üzerinde çok hızlı çalışabilen verimli dil modelleridir. Phi-3.5-mini, Microsoft tarafından geliştirilmiş 3.8 milyar (3.8B) parametreye sahip kompakt bir SLM'dir; düşük boyutuna rağmen yüksek mantıksal muhakeme, sıkı talimat takibi ve kanıta dayalı özetleme yeteneklerine sahiptir. Mehmet Burak Menteşe, Yerel RAG Asistanı projesinde SQLite'tan çekilen bilgileri sentezleyip Türkçe yanıtlar üretmek için 'phi-3.5-mini' modelini kullanmıştır.

## SQLite ve Sunucusuz (Serverless) Vektör Veritabanı Nedir?
Soru: SQLite nedir ve Mehmet Burak Menteşe Local RAG projesinde neden ChromaDB yerine SQLite tercih etmiştir?
Cevap: SQLite, harici bir veritabanı sunucusu veya Docker kurulumu gerektirmeyen (serverless / sunucusuz), tüm verileri yerel diskte tek bir hafif dosyada saklayan gömülü veritabanı motorudur. Mehmet Burak Menteşe, Yerel RAG Asistanı projesinde sistemi ek bağımlılıklardan uzak ve taşınabilir tutmak amacıyla ChromaDB veya Milvus gibi ağır sunucular yerine Python'un yerleşik 'sqlite3' kütüphanesini tercih etmiştir. Projede 'knowledge_base.db' içindeki 'documents' tablosunda metin içerikleri ('content') ve JSON formatında serileştirilmiş ('json.dumps') 1024 boyutlu vektörler ('embedding') yüksek hızda saklanmaktadır.

## Inference (Çıkarım) ve Çıkarım Süresi (Yanıt Hızı) Metrikleri Nedir?
Soru: Yapay zekada Inference (Çıkarım) nedir ve Mehmet Burak Menteşe'nin Local RAG asistanında çıkarım hızı kaç saniyedir?
Cevap: Inference (Çıkarım), eğitilmiş bir yapay zeka modelinin kullanıcıdan gelen yeni bir soruyu veya girdiyi işleyerek nihai bir cevap üretmesi sürecidir; çıkarım süresi ise modelin soruyu anlayıp yanıtı üretme hızını (latency) belirtir. Mehmet Burak Menteşe'nin Apple Silicon (MacBook Pro M4 Pro, 48 GB RAM) donanımı üzerinde yaptığı Local RAG Asistanı testlerinde genel yanıt süresi ortalama 0.5 - 1.5 saniye aralığında olup; doğrudan bilgi çekme soruları ortalama ~0.74 saniye, mantıksal çıkarım/yorumlama soruları ~1.09 saniye ve bağlam dışı soruları reddetme (refusal) süresi ~0.38 saniye olarak ölçülmüştür.

## Grounding (Zemine / Bağlama Oturtma) Nedir?
Soru: Yapay zekada Grounding (bağlama oturtma) nedir ve halüsinasyonu nasıl önler?
Cevap: Grounding, yapay zeka dil modelinin ürettiği cevapları kendi soyut eğitim ezberine veya genel varsayımlarına değil, kendisine o an sağlanan doğrulanmış somut belgelere (Context) ve gerçek kanıtlara dayandırması prensibidir. Mehmet Burak Menteşe'nin Local RAG Asistanı projesinde uyguladığı katı sistem promptu ve vektör arama yapısı, yanıtların %100 veritabanındaki '.md' belgelerine dayandırılmasını (grounding) sağlayarak halüsinasyonu ortadan kaldırır.

## Context Window (Bağlam Penceresi) ve Lost in the Middle Problemi Nedir?
Soru: Context Window (Bağlam Penceresi) ve Lost in the Middle (Ortada Kaybolma) problemi nedir?
Cevap: Context Window (Bağlam Penceresi), bir yapay zeka dil modelinin tek bir anda girdi ve çıktı olarak işleyebileceği maksimum metin ve belirteç (token) kapasitesidir; modelin 'kısa süreli hafızası' kabul edilir. Çok uzun belgeler tek seferde modele verildiğinde model ya hafıza sınırına takılır ya da metnin başını ve sonunu hatırlayıp ortadaki kritik bilgileri gözden kaçırır; buna 'Lost in the Middle' (Ortada Kaybolma) problemi denir. Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 2) blog yazısında açıklandığı üzere, RAG mimarisi belgeleri küçük parçalara (chunk) bölüp sadece en alakalı parçaları modele vererek bu sorunu çözer.

## FastAPI, Asenkron Fetch ve BM25 Hibrit Arama (Hybrid Search) Nedir?
Soru: FastAPI, Asenkron Fetch ve BM25 Hibrit Arama (Hybrid Search) nedir ve portfolyo asistanında nasıl kullanılmaktadır?
Cevap: FastAPI, Python ile yüksek hızlı ve modern web API sunucuları geliştirmek için kullanılan arka uç (backend) çatısıdır; Asenkron Fetch (JavaScript fetch API) ise web sayfasını yenilemeden arka plandaki sunucuyla canlı veri alışverişi yapılmasını sağlar. Mehmet Burak Menteşe'nin portfolyo sitesindeki (mburakmentese.dev) RAG sohbet asistanı, arka planda Python FastAPI sunucusu ve ön yüzde Vanilla JS asenkron fetch bağlantısı ile çalışmaktadır. BM25 ise kelime eşleşmesi tabanlı istatistiksel bir arama algoritmasıdır; BM25 ile anlamsal vektör aramasının (Cosine Similarity) birleştirilmesine Hibrit Arama (Hybrid Search) denir ve Mehmet Burak Menteşe'nin Local RAG projesinin gelecek geliştirme hedefleri arasındadır.

## Game Loop (Oyun Döngüsü) ve Multi-Threading (Çoklu İş Parçacığı) Nedir?
Soru: Game Loop (Oyun Döngüsü) ve Multi-threading nedir, GhostHunterINC oyununda nasıl kodlanmıştır?
Cevap: Game Loop (Oyun Döngüsü), bir video oyununun kalbini oluşturan ve oyun açık olduğu sürece kesintisiz çalışan ana yazılım döngüsüdür; her bir karede (frame) sırasıyla oyuncunun klavye/fare girdilerini okur (input), oyun dünyasındaki fizik ve hareket kurallarını günceller (update) ve son durumu ekrana çizer (render). Multi-threading (Çoklu İş Parçacığı) ise arayüzün donmasını önlemek için farklı görevlerin işlemci üzerinde eşzamanlı iş parçacıkları (thread) halinde çalıştırılmasıdır. Mehmet Burak Menteşe ve ekibinin hazır oyun motoru kullanmadan geliştirdiği GhostHunterINC (GhostHunterGame) projesinde, saniyede sabit 60 kare (60 FPS) hızında çalışan özel bir Java Thread ve Game Loop mimarisi sıfırdan yazılmıştır.

## Collision Detection (Çarpışma Tespiti) ve Bounding Box (AABB) Nedir?
Soru: Collision Detection (Çarpışma Tespiti) ve Bounding Box (Sınır Kutusu) nedir, GhostHunterINC oyununda nasıl uygulanmıştır?
Cevap: Collision Detection (Çarpışma Tespiti), 2D veya 3D sanal bir oyun uzayında iki ya da daha fazla nesnenin (örneğin oyuncu karakteri, hayaletler, duvarlar veya tarayıcı silah alanı) geometrik olarak birbiriyle temas edip etmediğini hesaplayan algoritmadır. Mehmet Burak Menteşe'nin bizzat görev aldığı GhostHunterINC oyun motorunda hazır bir fizik motoru kullanılmadığı için, nesneleri çevreleyen görünmez dikdörtgen sınır kutuları (Bounding Box / AABB) üzerinden matematiksel koordinat kesişim ve çarpışma hesaplamaları sıfırdan Java ile kodlanmıştır.

## Object Pooling (Nesne Havuzlama Tasarım Kalıbı) Nedir?
Soru: Object Pooling (Nesne Havuzlama) nedir ve oyun geliştirmede neden kullanılır?
Cevap: Object Pooling (Nesne Havuzlama), oyunlarda ve yüksek performanslı yazılımlarda sürekli oluşturulup yok edilen nesneleri (efektler, mermiler, partiküller, hayalet objeleri vb.) bellekten (RAM) sürekli silip yeniden üretmek yerine, önceden ayrılmış bir nesne havuzunda (pool) hazır tutarak ihtiyaç duyuldukça yeniden aktif eden bir yazılım tasarım kalıbıdır. Bu sayede Java'nın Çöp Toplayıcı (Garbage Collector) mekanizmasının ekranı donduran anlık takılmalar (lag spike) yaratması ve bellek sızıntıları engellenir; Mehmet Burak Menteşe'nin GhostHunterINC gibi Java/JavaFX tabanlı projelerinde performans optimizasyonu sağlar.

## Property Binding (Dinamik Özellik Bağlama ve Ekran Oranlama) Nedir?
Soru: Property Binding (Özellik Bağlama) ve Responsive Scaling nedir, GhostHunterINC projesinde hangi zorluğu çözmüştür?
Cevap: Property Binding, JavaFX mimarisinde bir nesnenin bir özelliğinin (örneğin bir oyun objesinin genişliği, yüksekliği veya X/Y koordinatının) başka bir nesnenin özelliğine (örneğin ana oyun penceresinin dinamik boyutuna) matematiksel olarak bağlanmasıdır. Mehmet Burak Menteşe ve ekibini GhostHunterINC oyununu geliştirirken en çok zorlayan teknik konu ekran oranlama (aspect ratio / responsive scaling) olmuş; pencere boyutu değiştiğinde veya farklı ekran çözünürlüklerinde oyun içi nesnelerin bozulmadan doğru koordinatlarda kalması JavaFX Property Binding algoritmalarıyla sıfırdan çözülmüştür.

## OOP (Nesne Yönelimli Programlama) ve 4 Temel İlkesi (Encapsulation, Inheritance, Polymorphism, Abstraction) Nedir?
Soru: OOP (Nesne Yönelimli Programlama) nedir ve 4 temel ilkesi (Kapsülleme, Kalıtım, Çok Biçimlilik, Soyutlama) ne anlama gelir?
Cevap: OOP (Object-Oriented Programming / Nesne Yönelimli Programlama), yazılım geliştirmede gerçek dünyadaki varlıkları sınıflar (classes) ve nesneler (objects) olarak modelleyen temel programlama paradigmasıdır ve 4 ana ilkeye dayanır: (1) Kapsülleme (Encapsulation): Verilerin sınıf içinde gizlenip sadece yetkili getter/setter metotlarıyla dışarı açılması; (2) Kalıtım (Inheritance): Bir alt sınıfın üst sınıfın özelliklerini ve davranışlarını miras alması; (3) Çok Biçimlilik (Polymorphism): Aynı isimli bir metodun farklı alt sınıflarda farklı davranışlar sergileyebilmesi (override); (4) Soyutlama (Abstraction): Karmaşık arka plan detaylarının gizlenip yalnızca gerekli arayüzün sunulması. Mehmet Burak Menteşe'nin Java ile geliştirdiği Library Management System ve GhostHunterINC projeleri bütünüyle OOP mimarisi üzerine inşa edilmiştir.

## Auth & Roles (Kimlik Doğrulama ve Rol Yönetimi) ile Exception Handling (Hata Yakalama) Nedir?
Soru: Auth & Roles (Rol Tabanlı Yetkilendirme) ve Exception Handling (İstisna / Hata Yönetimi) nedir, Kütüphane Yönetim Sistemi'nde nasıl kullanılmıştır?
Cevap: Auth & Roles (Authentication & Role-Based Access Control), bir yazılıma giriş yapan kullanıcıların kimliğinin doğrulanması ve sahip oldukları role (örneğin Admin/Yönetici veya standart User/Kullanıcı) göre farklı ekranlara ve işlem yetkilerine erişebilmesidir. Exception Handling (İstisna/Hata Yönetimi) ise program çalışırken oluşabilecek beklenmedik hataların (dosya bulunamaması, stokta olmayan kitabın ödünç alınması, hatalı girdi vb.) 'try-catch' bloklarıyla yakalanarak programın çökmesinin önlenmesidir. Mehmet Burak Menteşe, Library Management System projesinde Admin ve Kullanıcı panellerini ayırmak için Auth & Roles yapısını, JSON veri güvenliğini korumak için ise Exception Handling mekanizmasını kullanmıştır.

## GUI (Grafiksel Kullanıcı Arayüzü) vs CLI (Komut Satırı Arayüzü) Nedir?
Soru: GUI (Graphical User Interface) ve CLI (Command Line Interface) nedir, aralarındaki fark nedir?
Cevap: CLI (Command Line Interface / Komut Satırı Arayüzü), kullanıcının yazılımla yalnızca metin komutları yazarak etkileşime girdiği siyah terminal ekranıdır; çok hafiftir, hızlıdır ve otomasyona uygundur. GUI (Graphical User Interface / Grafiksel Kullanıcı Arayüzü) ise pencereler, butonlar, tablolar ve görseller içeren kullanıcı dostu grafiksel ekranlardır. Mehmet Burak Menteşe'nin portfolyosunda hem CLI tabanlı projeler (Yerel RAG Asistanı terminal uygulaması) hem de JavaFX ile geliştirilmiş modern GUI masaüstü yazılımları (Library Management System ve GhostHunterINC) yer almaktadır.

## TableView (JavaFX Dinamik Tablo Bileşeni) Nedir?
Soru: JavaFX TableView bileşeni nedir ve Kütüphane Yönetim Sistemi'nde ne işe yarar?
Cevap: TableView, JavaFX grafik kütüphanesinde verileri satır ve sütunlar halinde listeleyen, kullanıcının sütun başlıklarına tıklayarak sıralama yapabildiği ve arama kutusuyla anlık filtreleme sağlayabildiği dinamik tablo bileşenidir. Mehmet Burak Menteşe'nin Library Management System (Kütüphane Yönetim Sistemi) projesinde merkezi kütüphane kitap envanterinin, stok adetlerinin ve kullanıcıların ödünç aldığı kitap listelerinin ekranda canlı olarak gösterilmesinde TableView kullanılmıştır.

## DOM Manipulation (DOM Manipülasyonu) ve Accordion UI (Akordeon Arayüz) Nedir?
Soru: DOM Manipulation (DOM Manipülasyonu) ve Accordion UI (Akordeon Arayüz) nedir, Marmara Siber projesinde nasıl kullanılmıştır?
Cevap: DOM Manipulation (Belge Nesne Modeli Manipülasyonu), JavaScript kullanılarak bir web sayfasındaki HTML öğelerinin, metinlerin ve CSS stillerinin sayfa yenilenmeden canlı olarak değiştirilmesi veya güncellenmesi işlemidir. Accordion UI (Akordeon Arayüz) ise başlıkların alt alta dizildiği, tıklandığında yalnızca ilgili cevabın kayarak açıldığı dinamik arayüz bileşenidir. Mehmet Burak Menteşe, Marmara Siber Web Arayüzü (marmaracyber.com) projesinde dinamik Sıkça Sorulan Sorular (SSS / FAQ) bölümünü ve çift dilli çeviri sistemini saf Vanilla JS ile DOM Manipülasyonu ve Accordion UI kullanarak geliştirmiştir.

## Honeypot (Bal Küpü Bot Koruması) ve Formspree Nedir?
Soru: Honeypot (Bal Küpü) form güvenliği ve Formspree nedir, Marmara Siber sitesinde nasıl kullanılmıştır?
Cevap: Honeypot (Bal Küpü), web sitelerindeki iletişim ve başvuru formlarında gerçek insan kullanıcıların göremediği (CSS ile gizlenmiş), ancak internetteki otomatik spam botlarının kodları tararken doldurmaya çalıştığı tuzak bir girdi (input) alanıdır; bu gizli alan doldurulursa sistem isteğin bir bottan geldiğini anlayıp formu reddeder. Formspree ise ön yüz odaklı web sitelerinde güvenli form gönderimi sağlayan bir servistir. Mehmet Burak Menteşe, geliştirdiği Marmara Siber (marmaracyber.com) web sitesindeki iletişim formlarında spam bot saldırılarını önlemek için Honeypot ve Formspree entegrasyonu kullanmıştır.

## Input Sanitization (Girdi Temizleme) ve XSS (Cross-Site Scripting) Koruması Nedir?
Soru: Input Sanitization (Girdi Temizleme) ve XSS (Cross-Site Scripting) koruması nedir?
Cevap: Input Sanitization (Girdi Temizleme), web formlarına veya uygulama girdi alanlarına kullanıcılar tarafından yazılan metinlerin filtrelenerek, içerisinde bulunabilecek zararlı HTML, JavaScript veya SQL betiklerinden arındırılması işlemidir. Bu sayede saldırganların web sitesine zararlı kod enjekte etmesini amaçlayan XSS (Cross-Site Scripting) saldırıları engellenir. Mehmet Burak Menteşe, Siber Kulüpler Birliği Web Uygulama Güvenliği Eğitimi'nde edindiği güvenli kod yazımı (secure coding) prensipleri doğrultusunda Marmara Siber web sitesinde XSS koruması ve girdi temizleme önlemlerini uygulamıştır.

## Glassmorphism (Yarı Saydam Cam Tasarımı) ve Cyberpunk UI Nedir?
Soru: Glassmorphism (Yarı Saydam Cam Tasarımı) nedir ve Mehmet Burak Menteşe'nin web tasarımlarında nasıl uygulanmıştır?
Cevap: Glassmorphism, modern kullanıcı arayüzü (UI/UX) tasarımında kartların ve panellerin arka planının buzlu veya yarı saydam bir cam gibi görünmesini sağlayan (CSS 'backdrop-filter: blur' özelliğiyle), neon ışıklar ve ince parlak kenarlıklarla desteklenen fütüristik bir görsel tasarım stilidir. Mehmet Burak Menteşe'nin hem kişisel portfolyo sitesinde (mburakmentese.dev) hem de Marmara Siber platformunda (marmaracyber.com) siberpunk estetiğini yansıtmak amacıyla saf CSS3 ile sıfırdan kodlanmıştır.

## Responsive (Duyarlı / Mobil Uyumlu) Web Tasarımı, CSS Flexbox ve CSS Grid Nedir?
Soru: Responsive web tasarımı, CSS Flexbox ve CSS Grid nedir?
Cevap: Responsive (Duyarlı) tasarım, bir web sitesinin masaüstü bilgisayarlardan tabletlere ve akıllı telefonlara kadar tüm farklı ekran boyutlarına otomatik olarak uyum sağlaması ve içeriğin bozulmadan ölçeklenmesidir. CSS Flexbox öğeleri tek boyutta (satır veya sütun) esnek biçimde hizalarken, CSS Grid çok sütunlu kartları iki boyutlu (satır ve sütun) ızgara sistemiyle düzenler. Mehmet Burak Menteşe, Marmara Siber (marmaracyber.com) ve kişisel portfolyo (mburakmentese.dev) sitelerinde mobil uyumluluğu CSS Flexbox ve CSS Grid mimarileriyle sağlamıştır.

## Cloudflare CDN ve AES-256 Şifreleme Nedir?
Soru: Cloudflare CDN ve AES-256 şifreleme standardı nedir?
Cevap: Cloudflare CDN (Content Delivery Network / İçerik Dağıtım Ağı), bir web sitesinin içeriklerini dünya genelindeki sunucular üzerinden ziyaretçiye en yakın noktadan sunarak yüksek hız sağlayan ve aynı zamanda DDoS gibi siber saldırılara karşı koruma kalkanı oluşturan ağ altyapısıdır (mburakmentese.dev Cloudflare CDN üzerinden yayınlanmaktadır). AES-256 (Advanced Encryption Standard) ise 256 bit anahtar uzunluğu kullanan, günümüzde siber güvenlikte en güvenli kabul edilen simetrik şifreleme standardıdır ve Mehmet Burak Menteşe'nin geliştirdiği Marmara Siber web sitesinin tematik terminal durum çubuğunda simüle edilmiştir.

## OSINT (Açık Kaynak İstihbaratı), CTF (Capture The Flag) ve Sızma Testi (Penetration Testing) Araçları Nedir?
Soru: OSINT, CTF, Sızma Testi (Penetration Testing) ve Wireshark, Burp Suite, Bettercap araçları nedir?
Cevap: Siber güvenlikte OSINT (Open Source Intelligence), halka açık internet kaynaklarından siber istihbarat ve bilgi toplama metodolojisidir. CTF (Capture The Flag), siber güvenlik uzmanlarının zafiyetli sistemlerdeki güvenlik açıklarını bularak gizli bayrakları (flag) yakaladığı uygulamalı güvenlik yarışmalarıdır. Sızma Testi (Penetration Testing) ise bir sistemin güvenliğini test etmek için yetkili olarak saldırgan gözüyle zafiyet aranmasıdır. Mehmet Burak Menteşe, SyberTÜRK siber güvenlik stajında ağ trafiğini analiz eden Wireshark, web uygulaması trafiğini yakalayıp test eden Burp Suite ve yerel ağ analiz/MITM testleri yapan Bettercap araçlarını kullanarak 5'ten fazla sistemde temel sızma testi gerçekleştirmiş olup düzenli olarak CTF yarışmalarına katılmaktadır.

## NIC (Network Interface Card), OSI Modeli, OUI, Switch ve Router Nedir?
Soru: NIC (Ağ Kartı), OSI Modeli, OUI kodu, Switch ve Router kavramları nedir?
Cevap: Mehmet Burak Menteşe'nin 'MAC Adresi ve ARP' blog yazısında açıklandığı üzere; NIC (Network Interface Card / Ağ Arayüz Kartı), bir cihazın ağa bağlanmasını sağlayan ve üzerinde fabrikada yazılmış 48 bitlik fiziksel MAC adresini (ilk 6 hanesi üretici firmayı belirten OUI kodudur) barındıran donanım birimidir. OSI Referans Modeli ağ iletişimini 7 katmana ayırır: 1. Fiziksel katman bitleri taşır, 2. Veri Bağlantısı (Data Link) katmanı MAC adresleriyle yerel ağ (LAN) içi iletimi yapar (Switch bu katmanda çalışır), 3. Ağ (Network) katmanı ise IP adresleriyle paketleri dış ağlara/internete yönlendirir (Router bu katmanda çalışır).

## CIA Triad (Gizlilik, Bütünlük, Erişilebilirlik / CIA Üçlüsü) Nedir?
Soru: Siber güvenlikte CIA Triad (CIA Üçlüsü: Confidentiality, Integrity, Availability) nedir?
Cevap: Mehmet Burak Menteşe'nin 'Bilgi Güvenliği Modelleri ve CIA Üçlüsü' blog yazısında incelenen CIA Triad, bilgi güvenliğinin evrensel temelini oluşturan 3 ana ilkedir: (1) Confidentiality (Gizlilik): Hassas verilerin yalnızca yetkili kişilerce görülmesi ve yetkisiz kişilere ifşa edilmemesi; (2) Integrity (Bütünlük): Verilerin yetkisizce değiştirilmemesi, bozulmaması ve doğruluğunun korunması; (3) Availability (Erişilebilirlik): Sistemlerin ve bilgilerin yetkili kullanıcılar için ihtiyaç duyulan her an kesintisiz erişilebilir olması.

## Bell-LaPadula Modeli (No Read Up, No Write Down) Nedir?
Soru: Bell-LaPadula güvenlik modeli nedir, No Read Up ve No Write Down kuralları ne anlama gelir?
Cevap: Mehmet Burak Menteşe'nin 'Bilgi Güvenliği Modelleri ve CIA Üçlüsü' blog yazısında açıklanan Bell-LaPadula modeli, askeri ve kurumsal sistemlerde Gizliliği (Confidentiality) korumak için tasarlanmış güvenlik modelidir. Başlıca kuralları şunlardır: (1) No Read Up (Simple Security Property): Düşük güvenlik seviyesindeki bir özne, kendisinden yüksek seviyedeki gizli bir veriyi okuyamaz; (2) No Write Down (Star Security Property): Yüksek güvenlik seviyesindeki bir özne, gizli bilgileri sızdırmamak için daha düşük güvenlik seviyesindeki bir nesneye yazma işlemi yapamaz; (3) Discretionary-Security Property: Yetkileri erişim matrisiyle denetler.

## Biba Integrity Modeli (No Read Down, No Write Up) Nedir?
Soru: Biba Integrity güvenlik modeli nedir, No Read Down ve No Write Up kuralları ne anlama gelir?
Cevap: Mehmet Burak Menteşe'nin 'Bilgi Güvenliği Modelleri ve CIA Üçlüsü' blog yazısında yer alan Biba Modeli, sistemlerde veri Bütünlüğünü (Integrity) korumayı hedefleyen güvenlik modelidir ve Bell-LaPadula'nın tersi mantıkla çalışır: (1) No Read Down (Simple Integrity Property): Yüksek bütünlük seviyesindeki bir özne, düşük güvenilirlikli nesnelerden okuma yapamaz (güvenilir verinin kirlenmesini önler); (2) No Write Up (Star Integrity Property): Düşük bütünlük seviyesindeki bir özne, kendisinden daha yüksek bütünlüklü bir veriye yazamaz (temiz veriyi bozamaz).

## Clark-Wilson Modeli (CDI, UDI, TP, IVP) Nedir?
Soru: Clark-Wilson güvenlik modeli nedir, CDI, UDI, TP ve IVP kavramları ne işe yarar?
Cevap: Mehmet Burak Menteşe'nin 'Bilgi Güvenliği Modelleri ve CIA Üçlüsü' blog yazısında anlatılan Clark-Wilson modeli, ticari ve finansal sistemlerde veri bütünlüğünü (Integrity) sağlamak için geliştirilmiş bir güvenlik modelidir. Dört temel bileşen kullanır: bütünlüğü korunması zorunlu kritik veriler (CDI - Constrained Data Item), doğrulanmamış harici/kullanıcı girdileri (UDI - Unconstrained Data Item), verileri güvenli şekilde işleyen dönüşüm prosedürleri (TPs - Transformation Procedures) ve veri bütünlüğünü denetleyen doğrulama prosedürleri (IVPs - Integrity Verification Procedures).

## Brewer and Nash Modeli (Çin Duvarı / Chinese Wall Modeli) Nedir?
Soru: Brewer and Nash (Çin Duvarı / Chinese Wall) güvenlik modeli nedir?
Cevap: Mehmet Burak Menteşe'nin 'Bilgi Güvenliği Modelleri ve CIA Üçlüsü' blog yazısında bahsedilen Brewer and Nash (Çin Duvarı) modeli, finans, hukuk ve danışmanlık gibi ticari sektörlerde çıkar çatışmalarını (Conflict of Interest) önlemek amacıyla geliştirilmiş dinamik bir güvenlik modelidir. Bir kullanıcının erişebileceği veriler sabit değildir; kullanıcının daha önce eriştiği rakip şirket ve veri kümelerine bağlı olarak sistem tarafından dinamik şekilde sınırlandırılır.

## VPN (Sanal Özel Ağ / Virtual Private Network) ve Tünelleme (Tunneling) Nedir?
Soru: VPN (Virtual Private Network) ve Tünelleme (Tunneling) nedir, nasıl güvenlik sağlar?
Cevap: Mehmet Burak Menteşe'nin 'VPN ve Proxy Kavramları' blog yazısında açıklandığı üzere; VPN (Virtual Private Network / Sanal Özel Ağ), kullanıcı cihazı ile VPN sunucusu arasındaki tüm internet trafiğini güçlü kriptografik algoritmalarla şifreleyen özel bir veri hattıdır ve bu şifreli koridora 'Tünel' (Tunneling) adı verilir. İnternet Servis Sağlayıcıları (İSS / ISP) ve ağdaki üçüncü şahıslar VPN tünelinin içindeki verileri kesinlikle okuyamaz; ayrıca VPN yalnızca tarayıcıyı değil cihazdaki tüm işletim sistemi ve uygulama trafiğini kapsar.

## Proxy (Vekil Sunucu) Nedir?
Soru: Proxy (Vekil Sunucu) nedir ve VPN ile arasındaki temel fark nedir?
Cevap: Mehmet Burak Menteşe'nin 'VPN ve Proxy Kavramları' blog yazısında anlatıldığı üzere; Proxy (Vekil Sunucu), kullanıcı ile internet kaynakları arasında aracı olarak çalışan ve kullanıcının IP adresini maskeleyen bir sunucudur. Ancak VPN'den farklı olarak varsayılan iletişimi şifresizdir ve genellikle tüm işletim sistemini değil yalnızca yapılandırılan web tarayıcısını kapsar. Şifreleme yükü olmadığı için hızlıdır ancak İnternet Servis Sağlayıcıları (İSS / ISP) trafiği izleyebildiği için tam bir veri gizliliği sağlamaz.
