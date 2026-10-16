## Mehmet Burak Menteşe'nin GhostHunterINC Projesindeki Rolü ve Teknik Katkıları
Soru: Mehmet Burak Menteşe GhostHunterINC (GhostHunter) oyununda hangi görevleri üstlendi, ekipte ne yaptı ve projeye katkısı nedir?
Cevap: Mehmet Burak Menteşe, GhostHunterINC (GhostHunterGame) projesinde kullanıcı arayüzü (UI) ve menü tasarımlarını JavaFX ile sıfırdan geliştirmesinin yanı sıra, oyunun kendi özel oyun motorunun (custom game engine) önemli bir kısmını bizzat kodlamıştır. Özellikle oyun döngüsü (**Game Loop**), çarpışma tespiti (**Collision Detection**) ve özel fizik mimarisinin geliştirilmesinde doğrudan ve aktif rol oynamıştır.

## GhostHunterINC Oyununun Geliştirici Ekibi ve Ortak Geliştirme (Co-op Dev) Süreci
Soru: GhostHunterINC (GhostHunter) oyununu kimler geliştirdi, ekip kaç kişiden oluşuyor ve ekip arkadaşları kimlerdir?
Cevap: GhostHunterINC oyunu, Marmara Üniversitesi Bilgisayar Mühendisliği bölümünde eğitim gören 3 kişilik bir geliştirici ekibi tarafından ortaklaşa (**Co-op Dev**) geliştirilmiştir. Geliştirici ekip üyeleri **Mehmet Burak Menteşe**, **Mehmet Veli Kayıklı** ve **Eyüp Turhan**'dır. Geliştirme sürecinde Git ve GitHub kullanılarak profesyonel dal (branch), kod birleştirme (pull request/merge) ve görev yönetimi yürütülmüştür.

## GhostHunterINC Projesinin Ortaya Çıkışı ve Ders Projesinden Bağımsız Oyuna Dönüşmesi
Soru: GhostHunterINC (GhostHunter) oyunu nasıl ortaya çıktı, neden sadece bir üniversite ders projesi olarak kalmadı?
Cevap: GhostHunterINC projesinin temelleri, Mehmet Burak Menteşe ve ekip arkadaşlarının Marmara Üniversitesi Bilgisayar Mühendisliği bölümündeki Programming (Programlama) dersinin dönem projesi olarak atılmıştır. Proje tamamlanıp sunulduğunda dersin öğretim görevlileri (hocalar) oyunu çok beğenmiş ve takdir etmiştir. Bu yüksek beğeni üzerine Mehmet Burak Menteşe, Mehmet Veli Kayıklı ve Eyüp Turhan projeyi sadece dersi geçmekle sınırlı bırakmak istememiş; oyuna yeni mekanikler, yeni hayalet türleri ve ekstra özellikler ekleyerek tam teşekküllü, uzun soluklu bağımsız (indie) bir 2D hayatta kalma oyununa dönüştürmüştür.

## GhostHunterINC Geliştirilirken Karşılaşılan En Büyük Teknik Zorluk (Ekran Oranlama ve Property Binding)
Soru: GhostHunterINC (GhostHunter) oyunu geliştirilirken ekibi ve Mehmet Burak Menteşe'yi en çok zorlayan teknik problem neydi?
Cevap: GhostHunterINC geliştirilirken Mehmet Burak Menteşe ve ekibini en çok zorlayan teknik konu **ekran oranlama (aspect ratio / responsive scaling)** ve ekran boyutunu içerisindeki oyun objelerine dinamik olarak bağlama (**property binding**) kısmı olmuştur.
- **Property Binding (Özellik Bağlama) ve Responsive Scaling Nedir?** Hazır bir oyun motoru kullanılmadığı için, oyuncu oyun penceresinin boyutunu değiştirdiğinde veya oyun farklı ekran çözünürlüklerinde açıldığında; karakterlerin, haritanın, menülerin ve çarpışma kutularının (hitbox) bozulmadan, doğru koordinatlarda ve aynı görsel oranda kalmasını sağlayan dinamik matematiksel bağlama mekanizmasıdır. Ekip bu dinamik oranlama algoritmalarını JavaFX üzerinde sıfırdan geliştirmiştir.

## GhostHunterINC Neden Hazır Bir Oyun Motoru (Unity veya Unreal Engine) Olmadan Geliştirildi?
Soru: GhostHunterINC (GhostHunter) oyununda neden Unity veya Unreal Engine gibi hazır oyun motorları kullanılmadı?
Cevap: Mehmet Burak Menteşe ve ekibinin temel amacı sadece hazır araçlarla hızlıca bir oyun çıkarmak değil; nesne yönelimli programlama (**OOP**) prensiplerini, sahne geçişlerini, **sprite render** (2D görsel karakter ve nesne çizimi) mantığını, çoklu iş parçacığı (**multi-threading**) mimarisini ve oyun fiziğini mutfağında, yani sıfırdan kodlayarak öğrenmekti. Bu sebeple hazır oyun motorlarının arkasına saklanmak yerine standart kod editörlerinde saf **Java (Java 21)** ve **JavaFX** kullanarak kendi bağımsız 2D oyun motorlarını sıfırdan inşa etmişlerdir.

## GhostHunterINC Oyunu Oynanabilir Durumda mı, Gereksinimleri Neler ve Nereden İndirilebilir?
Soru: GhostHunterINC (GhostHunter / GhostHunterGame) oyunu şu an oynanabilir durumda mı, nasıl çalıştırılır ve kaynak kodlarını nereden indirebilirim?
Cevap: Evet, GhostHunterINC oyunu şu an tamamen çalışır ve oynanabilir durumdadır. Oyunu bilgisayarda çalıştırmak için **Java 21 veya daha güncel bir sürüm** yeterlidir. Oyunu denemek, çalıştırmak, forklamak veya kaynak kodlarını incelemek isteyen herkes doğrudan Mehmet Burak Menteşe'nin resmi GitHub deposuna (https://github.com/BurakHINGE/GhostHunterGame) erişebilir. Proje, **GhostHunter Community License v1.0** lisansı altında açık kaynak olarak paylaşılmaktadır.
