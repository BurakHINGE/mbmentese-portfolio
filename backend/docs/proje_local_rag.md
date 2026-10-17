## Yerel RAG Asistanı (Local RAG Asistanı / Local RAG Assistant) Genel Bakış:
**Yerel RAG Asistanı (Local RAG Asistanı / Local RAG Assistant)**, Mehmet Burak Menteşe tarafından geliştirilen, kişisel belgelerden bilgi çıkaran ve harici bir API veya internet bağlantısı kullanmadan tamamen kullanıcının kendi cihazı üzerinde (offline / yerel) çalışan **CLI (Komut Satırı Arayüzü)** tabanlı bir yapay zeka asistanıdır.
Proje, Mehmet Burak Menteşe'nin **Microsoft AI Innovators** yaz stajı kapsamında **Microsoft Foundry Local** ekosistemi ile **Python** kullanılarak sıfırdan tasarlanmıştır. Verileri buluta veya harici sunuculara göndermeden tamamen gizlilik odaklı (privacy-focused) çalışır ve ortalama **0.5 ile 1.5 saniye** arasında yanıt üretir.

## Yerel RAG Asistanının Çalışma Mantığı ve RAG Mimarisi:
Mehmet Burak Menteşe'nin geliştirdiği Yerel RAG Asistanı (Local RAG Asistanı) projesinde, büyük ve küçük dil modellerinin (LLM / SLM) bilmediği konularda uydurma cevaplar üretmesini (**Halüsinasyon / Hallucination**) önlemek amacıyla **RAG (Retrieval-Augmented Generation)** mimarisi kullanılmıştır. Sistemin çalışma süreci üç temel aşamadan oluşur:
1. **Parçalama (Chunking):** Kullanıcının kişisel belgeleri ve metin dosyaları anlam bütünlüğünü koruyacak şekilde anlamlı paragraflara ve metin parçalarına (chunk) ayrılır.
2. **Vektörleştirme (Embeddings) ve Kayıt:** Ayrılan metin parçaları **qwen3-embedding-0.6b** modeli kullanılarak çok boyutlu sayısal vektörlere dönüştürülür ve sunucusuz yerel **SQLite** veritabanında depolanır.
3. **Bulma ve Yanıt Üretme (Retrieval & Generation):** Kullanıcı bir soru sorduğunda soru da vektöre çevrilir; **Kosinüs Benzerliği (Cosine Similarity)** algoritması ile SQLite veritabanındaki en alakalı **metin parçaları (Top chunk'lar)** bulunur. Bu parçalar, sistem yönergesi (system prompt) ile birleştirilerek yerel **Phi-3.5 Mini (`phi-3.5-mini`)** dil modeline verilir ve yalnızca belgedeki kanıtlara dayalı Türkçe yanıt üretilir.

## Yerel RAG Asistanı Projesinde Kullanılan Teknolojiler:
Mehmet Burak Menteşe'nin Yerel RAG Asistanı (Local RAG Assistant) projesinde kullandığı temel teknolojiler ve sitedeki proje etiketleri (`Python`, `SQLite`, `RAG`, `Foundry Local`, `phi-3.5-mini`, `qwen3`, `Embeddings`, `Chunking`, `Cosine Similarity`) şunlardır:
1. **Python:** Veri işleme, metin parçalama (chunking), kosinüs benzerliği arama algoritması ve CLI/sunucu mimarisinin kodlanması.
2. **Microsoft Foundry Local SDK:** Yerel yapay zeka modellerinin bulut bağlantısı olmadan doğrudan cihaz donanımı (özellikle harici GPU gerektirmeden doğrudan CPU) üzerinde çalıştırılması ve yönetilmesi.
3. **Qwen3 Embedding Modeli (`qwen3-embedding-0.6b`):** Belgelerdeki metin parçalarını ve kullanıcının sorduğu soruları anlamsal arama için yüksek doğruluklu sayısal vektörlere dönüştüren model.
4. **Phi-3.5 Mini Dil Modeli (`phi-3.5-mini` SLM):** SQLite veritabanından getirilen en alakalı metin parçalarını sentezleyerek hızlı, doğru ve akıcı Türkçe yanıtlar üreten küçük dil modeli (Small Language Model).
5. **SQLite:** Vektörleri ve metin içeriklerini harici bir veritabanı sunucusu kurulumuna gerek kalmadan yerel diskte tek bir dosya halinde saklayan hafif veritabanı motoru.

## Yerel RAG Asistanının Amacı, Performansı ve Avantajları:
Mehmet Burak Menteşe'nin geliştirdiği Yerel RAG Asistanı (Local RAG Asistanı) projesinin en büyük avantajları **veri gizliliği, yüksek hız (0.5 - 1.5 saniye yanıt süresi) ve sıfır API maliyetidir**:
- **Tam Veri Gizliliği:** Hiçbir kişisel belge veya kullanıcı sorusu buluta ya da üçüncü taraf şirketlere (OpenAI vb.) gönderilmez; tüm işlem cihaz içinde gerçekleşir.
- **Çevrimdışı (Offline) Çalışma ve Sıfır Maliyet:** İnternet bağlantısı olmadan tamamen offline çalışabilir ve harici bir ücretli API anahtarı (API Key) gerektirmez.
- **Yüksek Hız:** Yerel donanım optimizasyonu sayesinde sorgular ortalama 0.5 ile 1.5 saniye gibi çok kısa sürelerde sonuçlanır.

## Yerel RAG Asistanı Projesinde Geçen Teknik Terimler Sözlüğü:
Ziyaretçilerin Mehmet Burak Menteşe'nin Yerel RAG Asistanı projesiyle ilgili sorabileceği teknik kavramlar ve açıklamaları:
- **RAG (Retrieval-Augmented Generation / Erişim Destekli Üretim):** Yapay zeka modeline soru sormadan önce ilgili bilgiyi güvenilir bir veritabanından bulup modelin önüne koyarak uydurma (halüsinasyon) yapmasını engelleyen mimaridir.
- **Chunking (Metin Parçalama):** Uzun belgelerin dil modelinin ve vektör aramasının daha kolay işleyebilmesi için anlamlı küçük paragraflara veya parçalara bölünmesi işlemidir.
- **Embeddings (Vektörleştirme):** Kelimelerin ve cümlelerin bilgisayarın anlamsal yakınlık kurabilmesi için sayı dizilerine (vektörlere) dönüştürülmesidir.
- **Cosine Similarity (Kosinüs Benzerliği):** İki metin vektörü arasındaki açının kosinüsünü hesaplayarak kullanıcının sorusu ile veritabanındaki metin parçalarının anlamca ne kadar birbirine benzediğini ölçen matematiksel formüldür.
- **SLM (Small Language Model / Küçük Dil Modeli):** `phi-3.5-mini` gibi daha az parametreye sahip, kişisel bilgisayarlarda yerel olarak çok hızlı çalışabilen verimli dil modelleridir.
- **CLI (Command Line Interface):** Uygulamanın grafiksel pencereler yerine doğrudan terminal / komut satırı ekranı üzerinden hızlı ve hafif şekilde kullanılmasını sağlayan arayüzdür.

## Yerel RAG Asistanı Bağlantıları ve Bilgiler:
Mehmet Burak Menteşe'nin Yerel RAG Asistanı (Local RAG Asistanı / Local RAG Assistant) projesiyle ilgili bağlantılar:
- **Portfolyo Proje Sayfası:** https://mburakmentese.dev/projeler
- **GitHub Profili:** https://github.com/BurakHINGE
