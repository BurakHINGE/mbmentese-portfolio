Local RAG Asistanı Projesinin Çıkış Hikayesi ve Microsoft AI Innovators Staj Süreci:
Soru: Local RAG projesi nasıl ortaya çıktı, Microsoft AI Innovators stajında süreç nasıldı ve proje nasıl geliştirildi?
Cevap: Mehmet Burak Menteşe, Microsoft AI Innovators stajına kabul aldıktan sonra düzenli aralıklarla gerçekleştirilen toplantılara katılmış ve genel staj programı bu toplantılarda aktarılmıştır. Staj, kapsamlı ve iyi hazırlanmış bir doküman üzerinden 3 farklı faza ayrılmış bir proje sürecini kapsıyordu. Stajyerlere farklı türde projeler seçme imkanı sunulmuştu; ancak RAG (Retrieval-Augmented Generation) konusu Mehmet Burak Menteşe'nin daha çok ilgisini çektiği için yerel bir RAG asistanı geliştirmeye karar vermiştir. Proje bir ekip çalışması değil, herkesin kendi projesini bağımsız olarak geliştirdiği kişisel (bireysel) bir projeydi.

Local RAG Projesinde Neden Bulut API Yerine Yerel Model Tercih Edildi:
Soru: Local RAG projesinde neden OpenAI veya benzeri bulut API'leri yerine yerel model tercih edildi?
Cevap: RAG sistemlerinin temel amacı yerel ortamda (localde) bulunan kişisel verilerle çalışmaktır. Dolayısıyla projenin kendisinde kullanıcının kendi yerel cihazından başka hiçbir harici servise ihtiyaç duyulmamaktadır. Bu nedenle harici bir bulut API'sine gerek duyulmamıştır. Bu yerel mimari sayesinde dışarıya hiçbir veri sızdırmayan, tamamen gizlilik odaklı, kullanım maliyeti olmayan (ücretsiz) ve çalışmak için internet bağlantısına gerek duymayan bağımsız bir yapay zeka asistanı geliştirilmiştir.

Local RAG Projesinin Donanım Gereksinimleri ve CPU Üzerinde Çalışma Mantığı:
Soru: Local RAG projesi pahalı bir ekran kartı (GPU) gerektirir mi, CPU üzerinde nasıl çalışıyor?
Cevap: Hayır, Local RAG asistanı pahalı bir GPU (ekran kartı) gerektirmez; sistem doğrudan işlemci (CPU) üzerinden çalışır. Mehmet Burak Menteşe'nin kendi kişisel bilgisayarı teknik açıdan bu alanda oldukça yüksek donanım yeterliliğine sahip olmasına rağmen, projenin herkesin bilgisayarında kolayca çalışabilmesini sağlamak amacıyla sistemi olabildiğince minimal sistem gereksinimlerine göre tasarlamış ve optimize etmiştir. Böylece standart dizüstü bilgisayarlarda ve Apple Silicon işlemcilerde rahatlıkla çalışabilmektedir.

Local RAG Projesinde Neden Vektör Veritabanı Olarak SQLite Tercih Edildi:
Soru: Local RAG projesinde neden ChromaDB veya Milvus yerine SQLite veritabanı kullanıldı?
Cevap: Projede harici bir veritabanı sunucusu kurulumu veya Docker gibi ek bağımlılıklara gerek duyulmaması ve yapılan incelemeler sonucunda SQLite'ın bu ölçekteki yerel belge aramaları için fazlasıyla yeterli olacağının görülmesi sebebiyle SQLite tercih edilmiştir. SQLite hem ekstra kurulum gerektirmeyen hafif ve taşınabilir bir yapı sunmuş hem de yerel kullanım için ideal bir hız-performans dengesi sağlamıştır.

Local RAG Geliştirilirken En Çok Zorlayan Konu ve Halüsinasyonun Engellenmesi:
Soru: Local RAG asistanı geliştirilirken en çok hangi konuda zorlanıldı ve halüsinasyon nasıl en aza indirildi?
Cevap: Proje geliştirilirken Mehmet Burak Menteşe'yi en çok zorlayan kısım yapay zekanın uydurma cevaplar üretmesini (halüsinasyonu) engelleme süreci olmuştur. Küçük parametreli modellerin yanlış bilgi üretme riskini en aza indirmek için çeşitli sistem promptları geliştirilmiş ve doğruluk (accuracy) hesaplamaları yapılarak modelin yalnızca sağlanan bağlama sadık kalması sağlanmıştır.

Portfolyo Web Sitesindeki Chatbot ile Local RAG Projesi Arasındaki İlişki:
Soru: Şu an konuştuğum portfolyo yapay zeka asistanı ile Local RAG projesi aynı şey mi?
Cevap: Evet, şu an web sitesinde kullanılan yapay zeka asistanı, Local RAG projesinde geliştirilen asistanla tamamen aynı altyapıya ve mimariye sahiptir. Hatta portfolyo web sitesine entegre edilen bu versiyon, veritabanı kapsamı ve belge hacmi açısından staj projesinden çok daha geniş ve kapsamlı bir hale getirilmiştir. Sistem, arka planda çalışan Python tabanlı bir FastAPI sunucusu ve ön yüzde saf (Vanilla) JavaScript asenkron fetch bağlantısı ile web sitesine entegre edilerek modern bir neon sohbet arayüzüne dönüştürülmüştür.

Local RAG Projesinin Gerçek Hayattaki Kullanım Alanları ve Gelecek Hedefleri:
Soru: Local RAG asistanı gerçek dünyada kimler için idealdir ve gelecekte projeye neler eklenecektir?
Cevap: Local RAG sistemi; verilerinin buluta çıkması KVKK veya GDPR gibi regülasyonlar nedeniyle yasak olan avukatlar, hukuk büroları, sağlık kuruluşları, hastaneler, finans ve denetim şirketleri ile internet bağlantısı bulunmayan sahada çalışan ekipler için ideal bir çözümdür. Mehmet Burak Menteşe, gelecekte bu projeye doğrudan PDF, Word ve metin dosyalarını yüklemeyi sağlayan bir dosya yükleme arayüzü ve arama kalitesini daha da artıran BM25 ile vektör aramasını birleştiren hibrit arama mimarisini eklemeyi hedeflemektedir.
