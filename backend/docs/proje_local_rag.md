Local RAG Asistanı Projesi Genel Bakış:
Local RAG Asistanı, Mehmet Burak Menteşe tarafından geliştirilen, tamamen kullanıcının kendi cihazı üzerinde (offline/yerel) çalışan ve belgeler üzerinden soruları yanıtlayan yeni nesil bir yapay zeka asistanıdır. Microsoft AI Innovators stajı ve Microsoft Foundry Local ekosistemi kapsamında tasarlanmış olup verileri harici sunuculara göndermeden gizlilik odaklı çalışır.

Local RAG Asistanının Çalışma Mantığı ve Mimarisi:
Büyük dil modellerinin (LLM) bilmediği konularda uydurma cevaplar üretmesini (Halüsinasyon) önlemek amacıyla RAG (Retrieval-Augmented Generation) mimarisi kullanılmıştır. Süreç üç aşamadan oluşur:
1. Parçalama (Chunking): Belgeler anlamlı paragraflara ayrılır.
2. Vektörleştirme (Embedding): Parçalar qwen3-embedding-0.6b modeli ile sayısal vektörlere çevrilip yerel SQLite veritabanında depolanır.
3. Bulma ve Üretme: Kullanıcı soru sorduğunda Kosinüs Benzerliği ile en alakalı 4 parça bulunur, bu parçalar sistem prompt'u ile birleştirilerek Phi-3.5 Mini modeline verilir ve kanıtlara dayalı yanıt üretilir.

Local RAG Asistanı Projesinde Kullanılan Teknolojiler:
Bu projede kullanılan temel teknolojiler şunlardır:
1. Python: Veri işleme, arama algoritması ve sunucu mimarisi.
2. Microsoft Foundry Local SDK: Yerel yapay zeka modellerinin cihaz üzerinde çalıştırılması ve yönetimi.
3. Qwen3 Embedding Modeli (qwen3-embedding-0.6b): Metinleri ve sorguları yüksek doğruluklu vektörlere dönüştürmek için.
4. Phi-3.5 Mini Dil Modeli (phi-3.5-mini): Veritabanından gelen bilgileri sentezleyip akıcı Türkçe yanıtlar üretmek için.
5. SQLite: Vektörleri ve içerikleri harici sunucu olmadan yerel diskte saklayan vektör veritabanı.

Local RAG Asistanının Amacı ve Avantajları:
En büyük avantajı gizlilik, hız ve sıfır maliyettir. Hiçbir kullanıcı verisi buluta veya üçüncü taraf şirketlere (OpenAI vb.) gitmez, internet bağlantısı olmadan da çalışabilir ve API kullanım ücreti gerektirmez.
