Kütüphane Yönetim Sistemi Projesinin Doğuşu ve Konsoldan JavaFX'e Geçiş Serüveni:
Soru: Kütüphane Yönetim Sistemi projesi nasıl ortaya çıktı, kişisel kitaplıktan merkezi kütüphaneye nasıl dönüştü?
Cevap: Proje ilk aşamada yalnızca kullanıcının kendi okuduğu kitapları kaydedebildiği basit bir "kişisel kitaplık" projesi olarak başlamıştır. Mehmet Burak Menteşe daha sonra projeyi gerçek ve kapsamlı bir merkezi kütüphane otomasyonuna dönüştürmeye karar vermiştir. Ancak eski kişisel kitap kaydetme yapısını kaldırmak yerine, mevcut yapıyı koruyarak üzerine merkezi kütüphane envanteri, ödünç alma (loan) sistemi ve admin yetkilendirme panelini eklemiştir. Ardından ilk başta konsol (terminal) tabanlı olan bu sistemi JavaFX teknolojisi ile modern, butonlu ve pencereli gerçek bir masaüstü grafik arayüzüne (GUI) dönüştürmüştür.

Kütüphane Yönetim Sisteminde Neden SQL Yerine JSON Kalıcılığı Tercih Edildi:
Soru: Kütüphane projesinde neden MySQL veya PostgreSQL yerine JSON dosyaları kullanıldı?
Cevap: Projenin ilk geliştirme aşamasında amaç sadece kitapları diske basitçe kaydetmek olduğu için JSON yapısı kullanılmıştır. Proje büyüdüğünde de harici bir SQL veritabanı sunucusu kurulumu gerektirmeden, verilerin hafif, taşınabilir, düzenli ve kolayca görüntülenebilir kalması amacıyla JSON altyapısı (users.json ve libraryBooks.json) başarıyla devam ettirilmiştir.

Kütüphane Sistemindeki Hibrit Raf ve Ödünç Alma (Loan) Etkileşimi:
Soru: Kütüphane Yönetim Sistemindeki hibrit raf sistemi nedir ve ödünç alma nasıl kurgulanmıştır?
Cevap: Mehmet Burak Menteşe'nin yaklaşımına göre: Bir kitap kütüphaneden ödünç alındıysa, mantıken o kişinin okuma listesine girmelidir. Projede hem merkezi kütüphane hem de kişisel kitaplık bulunduğu için bu iki yapı arasında doğrudan bir etkileşim kurgulanmıştır. Bir kullanıcı kütüphaneden kitap ödünç aldığında, kitap otomatik olarak kullanıcının kendi kişisel rafında "Okunuyor" statüsüyle listelenir.

Kütüphane Yönetim Sistemi Geliştirilirken Karşılaşılan En Büyük Teknik Zorluklar:
Soru: Kütüphane sistemi geliştirilirken Mehmet Burak Menteşe'yi en çok zorlayan teknik zorluklar nelerdi?
Cevap: Proje geliştirilirken en çok zorlayan kısım ödünç alma (loan) mekanizması olmuştur; kitapların hem kütüphane envanterinde hem de kullanıcıların ödünç listelerinde ayrı ayrı indekslenmesi ve stok takibinin senkronize edilmesi ciddi bir mantıksal çaba gerektirmiştir. Ayrıca kişisel kitaplıktan merkezi kütüphaneye geçerken ve en sonda JavaFX arayüzüne geçerken sık sık arayüz ve mimari değişiklikleri yapmak gerekmiştir.

Kütüphane Yönetim Sistemi Kaynak Kodları ve GitHub Deposu:
Soru: Kütüphane Yönetim Sistemi projesinin kaynak kodlarına nereden ulaşabilirim?
Cevap: Kütüphane Yönetim Sistemi projesinin tüm kaynak kodlarına ve Java dosyalarına resmi GitHub deposu olan https://github.com/BurakHINGE/LibraryManagementSystem bağlantısı üzerinden doğrudan ulaşılabilir.
