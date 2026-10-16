## Library Management System (Kütüphane Yönetim Sistemi) Projesi Genel Bakış:
**Library Management System (Kütüphane Yönetim Sistemi)**, Mehmet Burak Menteşe tarafından **Java** ve **JavaFX** kullanılarak geliştirilmiş, nesne yönelimli programlama (**OOP**) tabanlı kapsamlı bir masaüstü kütüphane otomasyon uygulamasıdır. Kitapların kişisel raflara dizilmesinden merkezi kütüphane envanter organizasyonuna kadar tüm süreçleri uçtan uca modeller.
Proje; kişisel kitaplık (raf) yönetimini, merkezi kütüphane envanterini, dinamik kopya/stok takibini, kitap ödünç alma mekanizmasını ve rol tabanlı yetkilendirilmiş (**Auth & Roles**) yönetici (Admin) panelini tek bir çatı altında birleştirir.

## Library Management System Konsoldan (CLI) JavaFX Masaüstü Arayüzüne (GUI) Geçiş Süreci:
Mehmet Burak Menteşe'nin geliştirdiği Library Management System (Kütüphane Yönetim Sistemi) projesi ilk aşamada üniversite eğitimi sırasında konsol (terminal / CLI) tabanlı bir uygulama olarak kodlanmıştır. Ancak Mehmet Burak Menteşe projeyi yalnızca konsol çıktısıyla sınırlı bırakmayarak kapsamlı bir mimari dönüşüme gitmiş; sistemi **JavaFX** teknolojisi ile modern, butonlu, çok pencereli (Scene/Stage) ve dinamik veri tablolarına (**TableView**) sahip profesyonel bir grafiksel kullanıcı arayüzüne (**GUI**) taşımıştır.

## Library Management System Projesinde Kullanılan Teknolojiler ve Mimari:
Mehmet Burak Menteşe'nin Library Management System (Kütüphane Yönetim Sistemi) projesinde kullandığı temel teknolojiler ve sitedeki proje etiketleri (`Java`, `OOP`, `JSON`, `Auth & Roles`, `Inheritance`, `Polymorphism`, `Exception Handling`) şunlardır:
1. **Java:** Uygulamanın arka plan iş mantığını (business logic) ve veri modellerini oluşturan temel nesne yönelimli programlama dili.
2. **JavaFX (Masaüstü GUI):** Modern grafiksel kullanıcı arayüzü, özel CSS stil tasarımları, dinamik **TableView** tabloları ve sahne/pencere (**Scene / Stage**) yönetimi.
3. **Nesne Yönelimli Programlama (OOP — Inheritance, Polymorphism, Encapsulation):** `Library`, `User` ve `Book` sınıfları arasında kalıtım (**Inheritance**), çok biçimlilik (**Polymorphism**) ve kapsülleme (**Encapsulation**) prensiplerine dayanan temiz, genişletilebilir mimari.
4. **Auth & Roles (Kimlik Doğrulama ve Rol Tabanlı Yetkilendirme):** Sisteme giriş yapan kişilerin kimliğini doğrulayan ve standart kullanıcı (**User**) ile yönetici (**Admin**) rollerine göre farklı ekranlar ve yetkiler açan güvenlik katmanı.
5. **JSON Kalıcılığı (JSON Persistence):** Verilerin harici bir SQL veritabanı sunucusu kurulumuna gerek kalmadan, taşınabilir ve hafif **JSON** dosyaları (`users.json` ve `libraryBooks.json`) üzerinden diske güvenli bir şekilde kaydedilip (serialization) uygulama açıldığında geri okunması (deserialization).
6. **Exception Handling (İstisna ve Hata Yönetimi):** Geçersiz kullanıcı girdilerini, stok dışı ödünç alma denemelerini ve JSON dosya okuma/yazma sırasındaki olası veri bozulmalarını engelleyen hata yakalama (`try-catch`) blokları.

## Library Management System Öne Çıkan Özellikleri ve Modülleri:
Mehmet Burak Menteşe'nin Kütüphane Yönetim Sistemi (Library Management System) uygulamasında yer alan ana modüller şunlardır:
- **Hibrit Raf Sistemi (Kişisel ve Kütüphane Rafları):** Kullanıcıların hem kendi sahip oldukları kişisel kitapları kaydetmesini hem de merkezi kütüphaneden ödünç aldıkları kitapları **"Okunuyor"** statüsüyle tek bir entegre rafta takip etmesini sağlar.
- **Dinamik Ödünç Alma ve Stok/Kopya Takibi:** Kütüphaneden bir kitap ödünç alındığında veya iade edildiğinde kitabın mevcut kopya sayısı dinamik olarak güncellenir; stokta kopyası kalmayan kitapların ödünç verilmesi sistem tarafından engellenir.
- **Rol Tabanlı Paneller (Admin Paneli vs Kullanıcı Paneli / Auth & Roles):**
  - **Kullanıcı Paneli:** Standart kullanıcılar kütüphane kataloğunda kitap arama, stoktaki kitapları ödünç alma/iade etme ve kendi kişisel raflarını yönetme yetkisine sahiptir.
  - **Admin Paneli:** Yönetici (Admin) rolündeki kullanıcılar merkezi kütüphaneye yeni kitap ekleme, mevcut kitapların stok/kopya sayılarını güncelleme, kayıtlı kullanıcıları görüntüleme ve tüm sistem envanterini yönetme yetkilerine sahiptir.

## Library Management System Projesinde Geçen Teknik Terimler Sözlüğü:
Ziyaretçilerin Mehmet Burak Menteşe'nin Library Management System projesiyle ilgili sorabileceği teknik kavramlar ve projedeki karşılıkları:
- **Inheritance (Kalıtım):** Bir sınıfın (örneğin farklı kullanıcı veya materyal tiplerinin) ortak özelliklerini ve metotlarını üst bir sınıftan miras alarak kod tekrarını önlemesi prensibidir.
- **Polymorphism (Çok Biçimlilik):** Aynı metot çağrısının, nesnenin türüne veya rolüne (örneğin normal kullanıcı ile Admin kullanıcısına) göre farklı davranışlar sergileyebilmesi yeteneğidir.
- **Encapsulation (Kapsülleme):** Sınıf içindeki hassas verilerin (örneğin kullanıcı şifresi veya kitap stok adedi) dışarıdan doğrudan değiştirilmesini engelleyip yalnızca kontrollü `getter` ve `setter` metotlarıyla erişime açılmasıdır.
- **JSON Persistence (`users.json` & `libraryBooks.json`):** Uygulama kapatılsa bile kullanıcı ve kitap verilerinin kaybolmaması için verilerin JSON formatında yerel diskte kalıcı olarak saklanmasıdır.
- **Exception Handling (`try-catch`):** Program çalışırken oluşabilecek beklenmedik hataların (dosya bulunamaması, hatalı veri tipi girilmesi vb.) programı çökertmeden yakalanıp kullanıcıya anlamlı uyarı mesajları gösterilmesidir.

## Library Management System GitHub Kaynak Kodu ve Bağlantılar:
Mehmet Burak Menteşe'nin Library Management System (Kütüphane Yönetim Sistemi) projesine erişmek veya kaynak kodlarını incelemek için resmi bağlantılar:
- **GitHub Proje Kaynak Kodu:** https://github.com/BurakHINGE/LibraryManagementSystem
- **Portfolyo Proje Sayfası:** https://mburakmentese.dev/projeler
- **GitHub Profili:** https://github.com/BurakHINGE
