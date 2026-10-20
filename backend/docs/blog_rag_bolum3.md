## Local RAG Asistanı (Bölüm 3 — Final) Blog Yazısı Genel Bakış ve Kapsamı
Soru: Mehmet Burak Menteşe'nin Local RAG Asistanı blog serisinin 3. bölümü (Final / Phase 3) neyi anlatıyor, ne zaman yayımlandı ve kapsamı nedir?
Cevap: Mehmet Burak Menteşe'nin 7 Eylül 2026 tarihinde kaleme aldığı **"Local RAG Asistanı Geliştirmek: Sistemi Test Etmek (Bölüm 3 — Final)"** (Medium başlığıyla **"Local RAG Asistanı Geliştirmek: Sistemi Test Etmek ve Sınırları Zorlamak (Bölüm 3 — Final)"**, İngilizce: **"Developing a Local RAG Assistant: Testing the System (Part 3 — Final)"**, sitedeki kart adıyla **Local RAG Asistanı (Final)** / **Local RAG Assistant (Final)**, bağlantı: `https://mburakmentese.dev/blog/local-RAG-bolum-3`) başlıklı makale, 6 haftalık Microsoft AI Innovators staj ve geliştirme sürecinin final aşamasını (**Phase 3: Test & Optimizasyon**) anlatır.
4 dakikalık okuma süresine sahip olan yazıda (Etiketler: `Testing`, `Optimization`, `Apple Silicon`, `Hallucination Resistance`, `Validation`, `Performance`); sistemin sınırlarını zorlayan uç senaryo (**edge case**) testleri, girdi doğrulama (**input validation**), halüsinasyon direnci deneyleri, Apple Silicon (MacBook Pro) donanım hız testleri ve projenin açık kaynak olarak yayınlanma süreci ele alınır.

## Local RAG Bölüm 3 (Phase 3): Sistemi Terletmek, Uç Senaryo (Edge Case) ve Gerçek Dünya Testleri
Soru: Mehmet Burak Menteşe Local RAG (Bölüm 3 / Phase 3) aşamasında hangi dayanıklılık, uç senaryo (edge case) ve güvenilirlik testlerini yapmıştır?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 3 — Final / Phase 3) blog yazısında vurguladığı üzere; bir yazılımın yalnızca ideal/normal akışta çalışması yeterli değildir, asıl mühendislik sistemin zayıf noktalarını ve sınırlarını (**edge cases / uç senaryoları**) bulmaktır. Bu doğrultuda Phase 3 aşamasında yerel RAG asistanı; beklenmeyen kullanıcı hatalarına, boş veya anlamsız girdilere (`ValueError` çökmelerine) ve yapay zekanın uydurma (**halüsinasyon**) eğilimine karşı gerçek dünya stres testlerine tabi tutulmuştur.

## Local RAG Bölüm 3 (1. Adım): Boşluk ve Anlamsız Girdiler Dayanıklılık Testi, `ValueError` Hatası ve `.strip()` Çözümü
Soru: Local RAG (Bölüm 3) asistanında boşluk ve anlamsız girdiler nasıl bir hataya (`ValueError`) yol açtı ve `app.py` içinde `.strip()` ile nasıl çözüldü?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 3 — Final / Phase 3) yazısının 1. test adımında aktardığı üzere; ilk testlerde kullanıcının terminalde yanlışlıkla boş `Enter` tuşuna basması, yalnızca boşluk (`space`) karakterleri bırakması veya rastgele karakterler (`asdasdasdasd`) girmesi durumunda, embedding modelinin boş girdiyi vektörleştiremeyip **`ValueError`** hatası fırlattığı ve programın aniden kapandığı tespit edilmiştir.
- **Input Validation (Girdi Doğrulama) ve `.strip()` Çözümü:** Bu çökmeyi önlemek için Mehmet Burak Menteşe, `app.py` içerisindeki sohbet döngüsüne Python'un metin başındaki ve sonundaki boşlukları temizleyen **`.strip()`** metodunu kullanan bir girdi doğrulama kontrolü eklemiştir: `if not user_input.strip(): print("🤖 Asistan: Lütfen geçerli bir soru sorun.\n"); continue`
Bu kontrol sayesinde sistem boş girdileri modele göndermeden yakalamış ve ani program çökmeleri tamamen engellenmiştir.

## Local RAG Bölüm 3 (2. Adım): Halüsinasyon Direnci Testi ve Tuzak Soru Deneyi (`I do not have this information`)
Soru: Mehmet Burak Menteşe Local RAG (Bölüm 3) yazısında asistanın halüsinasyon direncini nasıl test etti ve model bilmediği tuzak soruya ne yanıt verdi?
Cevap: Mehmet Burak Menteşe, Local RAG Asistanı (Bölüm 3 — Final / Phase 3) yazısının 2. adımında asistanın uydurma (halüsinasyon) direncini ölçmek için, staj projesindeki dar kapsamlı test dosyasında (`siber_notlar.txt`) cevabı yer almayan bir **tuzak soru deneyi** gerçekleştirmiştir. O test ortamındaki örnek metinde kulüp başkanlığı bilgisi yer almadığı için asistana tuzak olarak *"Siber Güvenlik Kulübü'nün başkanı kimdir?"* şeklinde bağlam dışı bir soru yöneltilmiştir.
- **Testin Sonucu:** İnternete bağlı veya kısıtlanmamış standart bir dil modeli genel ezberinden rastgele bir isim uydurmaya meyillidir. Ancak Mehmet Burak Menteşe'nin geliştirdiği Local RAG sistemi, İngilizce sistem promptundaki katı kurala sadık kalarak uydurma yapmamış ve 0.44 saniyede doğrudan **`"I do not have this information."`** yanıtını vermiştir. Böylece modelin sağlanan bağlam dışına çıkmadığı ve sıfır halüsinasyonla çalıştığı pratikte doğrulanmıştır.
*(Önemli Bağlam Ayrımı Notu: Bu örnek yalnızca blog yazısındaki CLI halüsinasyon testi deneyini anlatmaktadır. Mehmet Burak Menteşe'nin güncel portfolyo veritabanındaki bilgilere göre kendisi Marmara Üniversitesi Siber Güvenlik Kulübü'nde [MÜSİBER / Marmara Siber] **Akademi Komitesi Başkanı** olarak görev yapmaktadır ve kulübün resmi web sitesi `marmaracyber.com` ile siber güvenlik eğitim müfredatlarını yönetmektedir.)*

## Local RAG Bölüm 3: Apple Silicon (MacBook Pro) Hız Testi Sonuçları ve Performans Metrikleri
Soru: Mehmet Burak Menteşe'nin Local RAG asistanında hız testi sonuçları nedir, Apple Silicon (MacBook Pro) üzerinde yanıt süreleri kaç saniye ölçülmüştür?
Cevap: Mehmet Burak Menteşe'nin Local RAG Asistanı (Bölüm 3 — Final / Phase 3) blog yazısında paylaştığı üzere; Apple Silicon (**MacBook Pro M4 Pro**) donanımı üzerinde Python'un **`time`** kütüphanesiyle yapılan hassas hız ve performans ölçümleri (genel ortalaması **0.5 - 1.5 saniye** aralığında olmak üzere) soru tipine göre şu şekildedir:
- **Doğrudan Bilgi Çekme Sorusu (Direct Fact Retrieval):** Ortalama **~0.74 saniye**
- **Mantıksal Çıkarım / Yorumlama Sorusu (Reasoning):** Ortalama **~1.09 saniye**
- **Bağlam Dışı Soruları Reddetme (Refusal):** Ortalama **~0.38 saniye**
Harici bir bulut API'si çağrılmadığı için ağ gecikmesi (network latency) sıfırdır ve RAG mimarisiyle belgeler küçük parçalar (chunk) halinde işlendiği için tüm yanıtlar ~1 saniye civarında veya altında üretilmektedir.

## Local RAG Projesinin Tamamlanması, Açık Kaynak Yayın Süreci ve Bağlantılar
Soru: Mehmet Burak Menteşe'nin Local RAG Asistanı projesi açık kaynak olarak yayınlandı mı, blog yazısına ve kaynak kodlarına nereden ulaşılabilir?
Cevap: Evet, Mehmet Burak Menteşe tarafından 6 haftalık Microsoft AI Innovators yaz stajı süresince geliştirilen; %100 çevrimdışı (offline) çalışan, gizlilik odaklı ve sıfır halüsinasyonlu **Yerel RAG Asistanı (Local RAG Assistant)** projesi; tüm Python kaynak kodları (`ingest.py`, `retrieve.py`, `app.py`), mimari şemaları ve Türkçe-İngilizce çift dilli `README` dokümantasyonu ile birlikte GitHub üzerinde açık kaynak olarak yayınlanmıştır:
- **GitHub Kaynak Kodları:** `https://github.com/BurakHINGE/Local-RAG-Assistant` (Profil: `https://github.com/BurakHINGE`)
- **Portfolyo Blog Yazısı (Bölüm 3 — Final):** `https://mburakmentese.dev/blog/local-RAG-bolum-3`
- **Medium Blog Yazısı (Bölüm 3 — Final):** `https://medium.com/@burakmentese16/local-rag-asistan%C4%B1-geli%C5%9Ftirmek-sistemi-test-etmek-ve-s%C4%B1n%C4%B1rlar%C4%B1-zorlamak-b%C3%B6l%C3%BCm-3-final-182b5e36e382`
- **Portfolyo Proje Detay Sayfası:** `https://mburakmentese.dev/projeler/local-rag`
