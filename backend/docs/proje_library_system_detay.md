## Library Management System (Kütüphane Yönetim Sistemi) Projesinin Doğuşu ve Konsoldan JavaFX'e Geçiş Serüveni
Soru: Library Management System (Kütüphane Yönetim Sistemi) projesi nasıl ortaya çıktı, kişisel kitaplıktan merkezi kütüphaneye ve JavaFX arayüzüne nasıl dönüştü?
Cevap: Mehmet Burak Menteşe'nin geliştirdiği Library Management System projesi, ilk aşamada yalnızca kullanıcının kendi okuduğu kitapları kaydedebildiği basit bir "kişisel kitaplık" uygulaması olarak başlamıştır. Mehmet Burak Menteşe daha sonra projeyi gerçek ve kapsamlı bir merkezi kütüphane otomasyonuna dönüştürmeye karar vermiştir. Ancak eski kişisel kitap kaydetme yapısını silmek yerine mevcut mimariyi koruyarak üzerine merkezi kütüphane envanteri, ödünç alma (loan) sistemi ve admin yetkilendirme panelini (**Auth & Roles**) eklemiştir. Son aşamada ise başlangıçta konsol (terminal / CLI) tabanlı olan bu sistemi **JavaFX** teknolojisi ile modern, butonlu, pencereli ve dinamik tablolara sahip gerçek bir masaüstü grafik arayüzüne (**GUI**) dönüştürmüştür.

## Library Management System Projesinde Neden SQL Yerine JSON Kalıcılığı (JSON Persistence) Tercih Edildi?
Soru: Library Management System (Kütüphane Yönetim Sistemi) projesinde neden MySQL veya PostgreSQL gibi bir SQL veritabanı yerine JSON dosyaları kullanıldı, veriler nerede saklanıyor?
Cevap: Mehmet Burak Menteşe, Library Management System projesinin ilk geliştirme aşamasında kitapları diske hızlı ve yalın biçimde kaydetmek amacıyla **JSON** yapısını tercih etmiştir. Proje büyüyüp merkezi kütüphane ve kullanıcı yetkilendirme sistemine dönüştüğünde de; projeyi indiren kişilerin harici bir SQL veritabanı sunucusu kurmasına gerek kalmaması, verilerin hafif, taşınabilir, düzenli ve insan gözüyle kolayca okunabilir kalması amacıyla JSON veri kalıcılığı (**JSON Persistence** — `users.json` ve `libraryBooks.json`) mimarisini başarıyla sürdürmüştür. Veriler yerel diskte bu JSON dosyalarında saklanmaktadır.

## Library Management System'deki Hibrit Raf ve Ödünç Alma (Loan) Etkileşimi
Soru: Library Management System (Kütüphane Yönetim Sistemi) içindeki hibrit raf sistemi nedir ve ödünç alma (loan) süreci nasıl kurgulanmıştır?
Cevap: Mehmet Burak Menteşe'nin bu projedeki tasarım yaklaşımına göre; bir kitap merkezi kütüphaneden ödünç alındıysa, mantıken o kullanıcının kişisel okuma listesine de girmelidir. Uygulamada hem merkezi kütüphane envanteri hem de kişisel kitaplık bulunduğu için bu iki yapı arasında doğrudan bir etkileşim (hibrit raf sistemi) kurgulanmıştır. Bir kullanıcı merkezi kütüphaneden kitap ödünç aldığında, kütüphanedeki stok adedi düşerken ilgili kitap otomatik olarak kullanıcının kendi kişisel rafında **"Okunuyor"** statüsüyle listelenir.

## Library Management System'de OOP Prensipleri, Auth & Roles ve Exception Handling Kullanımı
Soru: Library Management System (Kütüphane Yönetim Sistemi) projesinde OOP (Inheritance, Polymorphism), Auth & Roles ve Exception Handling nasıl uygulandı?
Cevap: Mehmet Burak Menteşe, Library Management System mimarisini tamamen Nesne Yönelimli Programlama (**OOP**) prensipleri üzerine kurmuştur:
- **Inheritance (Kalıtım) ve Polymorphism (Çok Biçimlilik):** Sistemdeki temel varlıklar (`Library`, `User`, `Book`) ve farklı kullanıcı tipleri ortak özelliklerini kalıtımla devralırken, kullanıcı tipine göre metot davranışları çok biçimlilikle özelleştirilmiştir.
- **Auth & Roles (Kimlik Doğrulama ve Rol Yönetimi):** Giriş yapan kullanıcının rolüne göre (**Admin** veya **User**) erişebileceği ekranlar ayrıştırılmıştır; Admin yeni kitap ve stok eklerken, standart kullanıcı kitap ödünç alıp kendi rafını yönetir.
- **Exception Handling (Hata Yakalama):** Stokta kalmayan bir kitabın ödünç alınmaya çalışılması, geçersiz form girdileri veya JSON dosya okuma/yazma hataları `try-catch` bloklarıyla yakalanarak uygulamanın çökmesi engellenir.

## Library Management System Geliştirilirken Karşılaşılan En Büyük Teknik Zorluklar
Soru: Library Management System (Kütüphane Yönetim Sistemi) geliştirilirken Mehmet Burak Menteşe'yi en çok zorlayan teknik problemler nelerdi?
Cevap: Mehmet Burak Menteşe'yi proje sürecinde en çok zorlayan kısım **ödünç alma (loan) ve indeks senkronizasyonu** mekanizması olmuştur. Kitapların hem merkezi kütüphane envanterinde (`libraryBooks.json`) hem de kullanıcıların kişisel ödünç listelerinde (`users.json`) ayrı ayrı indekslenmesi ve stok takibinin hatasız senkronize edilmesi ciddi bir algoritmik çaba gerektirmiştir. Bunun yanı sıra projenin kişisel kitaplıktan merkezi kütüphaneye evrilmesi ve konsoldan **JavaFX** masaüstü arayüzüne taşınması sırasında yapılan kapsamlı mimari dönüşümler (refactoring) projenin en öğretici zorlukları olmuştur.

## Library Management System Kaynak Kodları ve GitHub Deposu
Soru: Library Management System (Kütüphane Yönetim Sistemi) projesinin kaynak kodlarına ve GitHub linkine nereden ulaşabilirim?
Cevap: Mehmet Burak Menteşe'nin geliştirdiği Library Management System (Kütüphane Yönetim Sistemi) projesinin tüm kaynak kodlarına, Java/JavaFX sınıflarına ve proje yapısına resmi GitHub deposu olan https://github.com/BurakHINGE/LibraryManagementSystem bağlantısı üzerinden doğrudan ulaşılabilir.
