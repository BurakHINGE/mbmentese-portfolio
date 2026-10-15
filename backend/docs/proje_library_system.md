Kütüphane Yönetim Sistemi (Library Management System) Projesi Genel Bakış:
Kütüphane Yönetim Sistemi, Mehmet Burak Menteşe tarafından Java programlama dili ile geliştirilmiş kapsamlı bir masaüstü kütüphane otomasyon yazılımıdır. Proje, kişisel kitaplık (raf) yönetimini merkezi bir kütüphane envanteri, kopya takibi, ödünç alma mekanizması ve yetkilendirilmiş admin paneli ile tek bir çatı altında birleştirir.

Kütüphane Yönetim Sistemi Konsoldan JavaFX Masaüstü Arayüzüne Geçiş Süreci:
Proje ilk aşamada üniversite eğitimi sırasında konsol (terminal) tabanlı olarak kodlanmıştır. Ancak Mehmet Burak Menteşe projeyi sadece konsol çıktısıyla sınırlı bırakmayarak büyük bir mimari güncellemeye gitmiş ve sistemi JavaFX teknolojisi ile modern, butonlu, pencereli ve dinamik tablolara (TableView) sahip profesyonel bir grafiksel kullanıcı arayüzüne (GUI) dönüştürmüştür.

Kütüphane Yönetim Sisteminde Kullanılan Teknolojiler:
Bu projede kullanılan temel teknolojiler ve mimariler şunlardır:
1. Java: Temel nesne yönelimli programlama dili.
2. JavaFX: Modern masaüstü grafiksel kullanıcı arayüzü (GUI), stil tasarımları ve sahne (Scene/Stage) yönetimi.
3. Nesne Yönelimli Programlama (OOP): Library, User, Book sınıfları arasında kalıtım (Inheritance), çok biçimlilik (Polymorphism) ve kapsülleme (Encapsulation) prensipleri.
4. JSON Kalıcılığı (JSON Persistence): Verilerin harici bir SQL sunucusu kurulumuna gerek kalmadan, taşınabilir ve hafif JSON dosyaları (users.json ve libraryBooks.json) üzerinden diske güvenle kaydedilip okunması.
5. Exception Handling: Kullanıcı hatalarını ve veri bozulmalarını engelleyen sağlam hata yakalama blokları.

Kütüphane Yönetim Sisteminin Öne Çıkan Özellikleri ve Modülleri:
- Hibrit Raf Sistemi: Kullanıcıların hem kendi okudukları kişisel kitapları kaydetmesini hem de merkezi kütüphaneden ödünç aldıkları kitapları 'Okunuyor' statüsüyle tek bir rafta takip etmesini sağlar.
- Ödünç Alma ve Stok Takibi: Kütüphanedeki kitapların kopya sayıları dinamik olarak düşer ve artar; stokta kalmayan kitaplar ödünç verilemez.
- Admin Paneli vs Kullanıcı Paneli: Normal kullanıcılar kitap arama, ödünç alma ve kendi raflarını yönetme yetkisine sahipken; admin kullanıcıları yeni kitap ekleme, stok güncelleme, kullanıcıları görüntüleme ve sistem envanterini yönetme yetkilerine sahiptir.
