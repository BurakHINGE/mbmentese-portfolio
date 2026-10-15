Mehmet Burak Menteşe'nin GhostHunter Projesindeki Rolü ve Teknik Katkıları:
Soru: Mehmet Burak Menteşe GhostHunter oyununda hangi görevleri üstlendi, ekipte ne yaptı?
Cevap: Mehmet Burak Menteşe, GhostHunter projesinde kullanıcı arayüzü (UI) ve menü tasarımlarını sıfırdan geliştirmesinin yanı sıra, oyun motorunun (game engine) da önemli bir kısmını bizzat geliştirmiştir. Oyun döngüsü (game loop), çarpışma tespiti (collision detection) ve fizik mimarisinin kodlanmasında doğrudan ve aktif rol oynamıştır.

GhostHunter Oyununun Geliştirici Ekibi ve Co-op Geliştirme Süreci:
Soru: GhostHunter oyununu kimler geliştirdi, ekip kaç kişiden oluşuyor?
Cevap: GhostHunter oyunu, Marmara Üniversitesi Bilgisayar Mühendisliği bölümünde eğitim gören 3 kişilik bir geliştirici ekibi tarafından ortaklaşa (Co-op Dev) geliştirilmiştir. Ekip üyeleri Mehmet Burak Menteşe, Mehmet Veli Kayıklı ve Eyüp Turhan'dır. Geliştirme sürecinde Git ve GitHub kullanılarak profesyonel branch ve görev yönetimi yürütülmüştür.

GhostHunter Projesinin Ortaya Çıkışı ve Üniversite Dersinden Bağımsız Oyuna Dönüşmesi:
Soru: GhostHunter oyunu nasıl ortaya çıktı, neden sadece bir ders projesi olarak kalmadı?
Cevap: GhostHunter projesinin temelleri Marmara Üniversitesi'ndeki Programming (Programlama) dersinin dönem projesi olarak atılmıştır. Proje tamamlanıp sunulduğunda dersin öğretim görevlileri (hocalar) oyunu çok beğenmiş ve takdir etmiştir. Bu yüksek beğeni üzerine ekip projeyi sadece dersi geçmekle sınırlı bırakmak istememiş, oyuna yeni mekanikler, yeni hayalet türleri ve ekstra özellikler ekleyerek tam teşekküllü, uzun soluklu bağımsız bir 2D hayatta kalma oyununa dönüştürmüştür.

GhostHunter Geliştirilirken Karşılaşılan En Büyük Teknik Zorluk (Ekran Oranlama ve Obje Binding):
Soru: GhostHunter oyunu geliştirilirken ekibi ve Mehmet Burak'ı en çok zorlayan teknik problem neydi?
Cevap: Proje geliştirilirken ekibi en çok zorlayan teknik konu ekran oranlama (aspect ratio / responsive scaling) ve ekran boyutunu içerisindeki oyun objelerine dinamik olarak bağlama (property binding) kısmı olmuştur. Hazır bir oyun motoru kullanılmadığı için pencere boyutu değiştiğinde veya farklı ekran çözünürlüklerinde oyun içi nesnelerin bozulmadan, doğru koordinatlarda ve aynı görsel oranda kalmasını sağlamak amacıyla dinamik bağlama algoritmaları sıfırdan geliştirilmiştir.

GhostHunter Neden Hazır Bir Oyun Motoru (Unity veya Unreal) Olmadan Geliştirildi:
Soru: GhostHunter oyununda neden Unity veya Unreal Engine gibi hazır oyun motorları kullanılmadı?
Cevap: Ekibin temel amacı sadece hazır araçlarla hızlı bir oyun çıkarmak değil, nesne yönelimli programlama (OOP) prensiplerini, sahne geçişlerini, sprite render mantığını, çoklu iş parçacığı (multi-threading) mimarisini ve oyun fiziğini mutfağında, yani sıfırdan kodlayarak öğrenmekti. Bu sebeple hazır motorların arkasına saklanmak yerine saf Java ve JavaFX (Java 21) kullanarak kendi bağımsız 2D motorlarını sıfırdan inşa etmişlerdir.

GhostHunter Oyunu Oynanabilir Durumda mı ve Nereden İndirilebilir:
Soru: GhostHunter oyunu şu an oynanabilir durumda mı, kaynak kodları ve oyunu nereden indirebilirim?
Cevap: Evet, GhostHunter oyunu şu an tamamen çalışır ve oynanabilir durumdadır. Oyunu denemek, çalıştırmak veya kaynak kodlarını incelemek isteyen herkes doğrudan projenin resmi GitHub deposuna (https://github.com/BurakHINGE/GhostHunterGame) erişebilir.
