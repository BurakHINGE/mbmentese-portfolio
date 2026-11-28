## GhostHunterINC (GhostHunter INC. / GhostHunterGame) Projesi Genel Bakış ve Amacı:
**GhostHunterINC** (veya **GhostHunter INC.** / **GhostHunterGame**), Mehmet Burak Menteşe ve 2 geliştirici arkadaşının (Mehmet Veli Kayıklı, Eyüp Turhan - toplam 3 kişilik bir ekip / Co-op Dev) ortaklaşa geliştirdiği, 2D bağımsız (indie) hayalet avlama, korku ve hayatta kalma oyunudur.
Projenin temelleri Marmara Üniversitesi Bilgisayar Mühendisliği bölümündeki programlama dersinin dönem projesi olarak atılmıştır; ancak Mehmet Burak Menteşe ve ekibi projeyi yalnızca ders kapsamında bırakmayıp mimarisini genişleterek tam teşekküllü, uzun soluklu bir bağımsız oyun projesine dönüştürmüştür.
*Önemli Ayrım Notu:* Mehmet Burak Menteşe'nin Sosyal Teknoloji Kulübü'nde 15-20 kişilik bir ekiple Unity oyun motoru ve C# kullanarak geliştirdiği kulüp oyunundan farklı olarak; **GhostHunterINC**, 3 kişilik bir ekiple hiçbir hazır oyun motoru kullanılmadan standart editörlerde tamamen sıfırdan **Java (Java 21+) ve JavaFX** ile kodlanmıştır.

## GhostHunterINC Projesinde Kullanılan Teknolojiler ve Oyun Motorsuz (No Game Engine) Mimari:
Mehmet Burak Menteşe'nin geliştirdiği GhostHunterINC projesinin en dikkat çekici mühendislik yönü, Unity, Unreal Engine veya Godot gibi hazır hiçbir harici oyun motoru (**No Game Engine**) kullanılmadan, standart kod editörlerinde tamamen sıfırdan inşa edilmiş olmasıdır. Tüm oyun mimarisi, özel fizik mekanikleri, çarpışma algılama (collision detection), kare hızı senkronizasyonu ve interaktif arayüzler **Java (Java 21+)** ve **JavaFX** kullanılarak kodlanmıştır.
Projede yer alan temel teknolojiler ve etiketler (`Java`, `JavaFX`, `OOP`, `2D Game Dev`, `No Game Engine`, `Game Loop`, `Co-op Dev`):
- **Java (Java 21) ve JavaFX:** Oyun penceresi, 2D grafik sahnesi (Canvas/Scene), interaktif menüler, butonlar ve görsel efektlerin sıfırdan oluşturulması.
- **Özel Game Loop (Oyun Döngüsü) ve Multi-Threading (Çoklu İş Parçacığı):** Oyun dünyasındaki fizik güncellemelerini, karakter/hayalet hareketlerini ve ekran yenileme kare hızını (FPS) donmadan, eşzamanlı olarak yöneten özel iş parçacığı (thread) mimarisi.
- **Nesne Yönelimli Programlama (OOP):** Farklı hayalet türleri, tarayıcı silahlar, harita engelleri ve oyuncu sınıfları arasında kalıtım (inheritance) ve çok biçimlilik (polymorphism) ilkelerine dayanan modüler sınıf yapısı.
- **Özel Fizik ve Collision Detection (Çarpışma Algılama):** Hazır bir fizik motoru olmadan, oyuncunun duvarlarla, engellerle ve hayaletlerle olan temasını koordinat ve sınır kutuları (bounding box) üzerinden hesaplayan matematiksel yapı.
- **Git ve GitHub (Co-op Dev / Ortak Geliştirme):** 3 kişilik geliştirici ekibinin branch (dal) yönetimi, kod birleştirme (merge/pull request) ve görev dağılımı süreçlerini yürüttüğü versiyon kontrol altyapısı.

## GhostHunterINC Oyununun Temel Mekanikleri ve Oynanış Özellikleri:
Mehmet Burak Menteşe'nin geliştirdiği GhostHunterINC (GhostHunterGame) oyunundaki temel oynanış (gameplay) dinamikleri şunlardır:
- **Görünmez Tehditler ve Keşif:** Oyuncu 2D perili mekanlarda (haunted locations) gezinirken çıplak gözle görülemeyen paranormal varlıkları ve hayaletleri özel tarayıcı ekipman yardımıyla tespit etmeye çalışır.
- **Tarayıcı Silah (Scanner Gun) ve Savaş (Combat) Sistemi:** Geleneksel ateşli silahlar yerine, görünmez hayaletleri tarayıp tespit ettikten sonra silahın içine çekerek (vakum/yakalama mekaniğiyle) etkisiz hale getirmeye dayalı özgün bir çatışma sistemi bulunur.
- **Dinamik Zorluk Seviyesi ve Hayatta Kalma:** Bölümler ilerledikçe hızlanan, davranış kalıpları farklılaşan ve oyuncuyu köşeye sıkıştıran yeni hayalet türleri ile artan bir aksiyon temposu sunulur.
- **Özgün Indie Arayüz (UI):** Retro ve modern bağımsız (indie) oyun estetiğini harmanlayan, JavaFX ile özelleştirilmiş kullanıcı dostu menüler ve oyun içi göstergeler (HUD) içerir.

## GhostHunterINC Projesinde Geçen Teknik Terimler ve Tanımlar:
Ziyaretçilerin Mehmet Burak Menteşe'nin GhostHunterINC projesiyle ilgili sorabileceği teknik terimler ve açıklamaları şunlardır:
- **Game Loop (Oyun Döngüsü):** Bir oyunun çalıştığı süre boyunca saniyede onlarca kez (örneğin 60 FPS) tekrarlanan; kullanıcı girdilerini okuma (input), oyun fiziğini ve durumunu güncelleme (update) ve görüntüyü ekrana çizme (render) adımlarını yöneten ana kalp atışı döngüsüdür.
- **Collision Detection (Çarpışma Algılama):** 2D veya 3D oyun dünyasındaki iki nesnenin (örneğin oyuncu ile duvarın veya silah ışını ile hayaletin) birbirine değip değmediğini matematiksel koordinat kesişimleriyle tespit eden algoritmadır.
- **JavaFX:** Java platformu üzerinde zengin grafiksel kullanıcı arayüzleri (GUI) ve 2D medya/oyun uygulamaları geliştirmek için kullanılan modern grafik kütüphanesidir.
- **Multi-threading (Çoklu İş Parçacığı):** Oyunun arayüzünün donmasını engellemek için grafik çizimi, ses/fizik hesaplamaları ve zamanlayıcıların işlemci üzerinde eşzamanlı iş parçacıkları (thread) halinde çalıştırılmasıdır.

## GhostHunterINC GitHub Kaynak Kodu, Bağlantılar ve Lisans:
Mehmet Burak Menteşe'nin GhostHunterINC projesine erişmek, oyunu indirmek veya kaynak kodlarını incelemek için resmi bağlantılar:
- **Proje Adı:** GhostHunterINC (GhostHunter INC. / GhostHunterGame)
- **GitHub Kaynak Kodu ve İndirme Bağlantısı:** https://github.com/BurakHINGE/GhostHunterGame
- **Portfolyo Proje Sayfası:** https://mburakmentese.dev/projeler
- **Sistem Gereksinimleri ve Lisans:** Java 21 veya üzeri, Git; GhostHunter Community License v1.0.
