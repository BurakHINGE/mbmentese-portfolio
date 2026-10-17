## Marmara Siber Web Arayüzü (Marmara Cyber Web Interface / marmaracyber.com) Genel Bakış:
**Marmara Siber Web Arayüzü** (**Marmara Cyber Web Interface** / **Marmara Cyber Web Sitesi** — `https://marmaracyber.com`), **Marmara Üniversitesi Siber Güvenlik Kulübü'nün (MÜSİBER / Marmara Siber)** resmi kurumsal web platformudur.
Mehmet Burak Menteşe, kulüpte **Akademi Komitesi Başkanı** olarak görev yaptığı ve kulübün teknik projelerinden sorumlu olduğu için kulübün web sitesini ve akordeon tarzı dinamik SSS (FAQ) bölümü ile `i18n` çeviri altyapısına sahip fütüristik arayüz geliştirmelerini sıfırdan inşa etmiştir. Bu proje, kulübün etkinliklerini, yönetim/komite kadrosunu, akademik çalışmalarını ve projelerini sergileyerek topluluğun dijital yüzünü oluşturur. *(Önemli Ayrım Notu: Bu proje Marmara Üniversitesi Siber Güvenlik Kulübü'nün kurumsal web sitesi olan `marmaracyber.com` içindir; Mehmet Burak Menteşe'nin kendi kişisel portfolyo web sitesi olan `mburakmentese.dev`'den ayrı bir projedir.)*

## Marmara Siber Web Arayüzü Projesinde Kullanılan Teknolojiler:
Mehmet Burak Menteşe'nin Marmara Siber (`marmaracyber.com`) projesinde kullandığı teknolojiler ve portfolyo kartındaki etiketler (`Vanilla JS`, `HTML5/CSS3`, `i18n`, `UI/UX Design`, `Responsive`, `DOM Manipulation`, `Accordion UI`) şunlardır:
- **HTML5:** Semantik, erişilebilir ve modern web sayfası iskeleti.
- **CSS3 & UI/UX Design (Kullanıcı Arayüzü ve Deneyimi Tasarımı):** Siber güvenliğe uygun fütüristik cyberpunk ve terminal estetiği, neon renk paleti, buzlu cam efekti (**Glassmorphism**) ve tüm ekran boyutlarına (mobil, tablet, masaüstü) uyum sağlayan **Responsive** (CSS Grid ve Flexbox) tasarım.
- **Vanilla JavaScript & DOM Manipulation:** Harici hiçbir ağır framework (React, Vue vb.) kullanmadan; sayfayı yeniden yüklemeden çalışan anahtar-değer (key-value) tabanlı dinamik çift dilli (TR/EN) çeviri motoru (**i18n**), akordeon SSS menüleri (**Accordion UI**) ve interaktif **DOM manipülasyonu**.
- **Formspree Entegrasyonu ve Güvenlik Katmanı:** Kulüp iletişim ve başvuru formlarının sunucusuz olarak güvenli gönderimi, girdi sanitizasyonu ile **XSS (Cross-Site Scripting)** koruması ve otomatik spam botlarını engelleyen gizli **Honeypot (Bal Küpü)** güvenlik mekanizması.

## Marmara Siber Web Sitesinin (`marmaracyber.com`) Özellikleri ve Bölümleri:
Mehmet Burak Menteşe tarafından geliştirilen Marmara Siber Web Arayüzü (`marmaracyber.com`) projesinde yer alan başlıca bölümler ve fonksiyonlar şunlardır:
- **Akordeon Tarzı Dinamik SSS Bölümü (Akordiyon S.S.S. / Accordion UI / FAQ):** Kulübe yeni katılacak öğrencilerin en sık sorduğu soruların (*"Yazılım geçmişim yok, sıfırdan zorlanır mıyım?"*, *"İngilizcem iyi değil, bu bir engel mi?"*, *"Yapay zeka siber güvenliğin önünü kapatıyor mu?"*, *"Bilgisayar Mühendisliği ile Siber Güvenlik Mühendisliği arasındaki fark nedir?"* vb.) tıklandığında pürüzsüz animasyonla açılıp kapanan akordeon kartlarla yanıtlandığı interaktif bölüm.
- **Terminal Arayüzü ve Durum Çubuğu (Status Bar):** Siber güvenlik temasına uygun **AES-256** şifreleme göstergeleri ve canlı sistem durumu simülasyonu içeren fütüristik tasarım.
- **Hiyerarşik Ekip ve Organizasyon Şeması:** Kulüp başkanı, başkan yardımcısı, sekreter ve komite başkanlarının (Akademi Komitesi Başkanı Mehmet Burak Menteşe dahil) kademeli olarak sergilendiği şeffaf yönetim ve ekip yapısı.
- **Güvenli ve Dinamik İletişim / Başvuru Formları:** Öğrencilerin ve ziyaretçilerin kulüple iletişim kurabileceği, etkinliklere ve komitelere başvurabileceği girdi sanitizasyonlu ve honeypot korumalı form alanları.
- **Dinamik Çift Dil Desteği (i18n - TR / EN):** Sayfa yenilenmeden Türkçe ve İngilizce dilleri arasında anlık geçiş sağlayan çoklu dil altyapısı.

## Marmara Siber Projesinde Geçen Teknik ve Siber Güvenlik Terimleri Sözlüğü:
Ziyaretçilerin Mehmet Burak Menteşe'nin Marmara Siber Web Arayüzü (`marmaracyber.com`) proje kartında veya açıklamasında görüp sorabileceği teknik kavramlar:
- **DOM Manipulation (DOM Manipülasyonu):** JavaScript kullanılarak web sayfasındaki HTML öğelerinin, metinlerin, sınıfların ve stillerin sayfa yenilenmeden canlı olarak değiştirilmesi, açılıp kapatılması veya güncellenmesi işlemidir.
- **Accordion UI (Akordeon / Akordiyon Arayüz):** Sayfada çok yer kaplamaması için başlıkların alt alta dizildiği, kullanıcı bir başlığa tıkladığında yalnızca ilgili içeriğin kayarak açıldığı ve diğerlerinin kapandığı dinamik arayüz bileşenidir (`marmaracyber.com` Sıkça Sorulan Sorular bölümünde kullanılmıştır).
- **XSS (Cross-Site Scripting) Koruması ve Girdi Sanitizasyonu (Input Sanitization):** Saldırganların iletişim formlarına veya girdi alanlarına zararlı JavaScript kodları enjekte ederek siteyi veya kullanıcıları hedef almasını engelleyen güvenlik önlemidir.
- **Honeypot (Bal Küpü Bot Koruması):** İletişim formlarının içine normal insan kullanıcıların görmediği ancak otomatik spam botlarının doldurduğu gizli bir alan ekleyerek, o alanı dolduran otomatik bot isteklerini tespit edip reddeden güvenlik tekniğidir.
- **Formspree:** Statik veya ön yüz odaklı web sitelerinde arka uç (backend) kodu yazmaya gerek kalmadan iletişim formlarını güvenli şekilde e-postaya ve panele yönlendiren form servisidir.
- **AES-256 (Advanced Encryption Standard):** 256 bit anahtar uzunluğu kullanan, günümüzde siber güvenlikte ve askeri/finansal iletişimde en güvenli kabul edilen simetrik şifreleme standardıdır.

## Marmara Siber Web Arayüzü (`marmaracyber.com`) Canlı Site ve Bağlantılar:
Mehmet Burak Menteşe'nin geliştirdiği Marmara Üniversitesi Siber Güvenlik Kulübü (MÜSİBER / Marmara Siber) web arayüzü projesine erişmek için resmi bağlantılar:
- **Canlı Kulüp Web Sitesi:** https://marmaracyber.com/
- **Portfolyo Proje Detay Sayfası:** https://mburakmentese.dev/projeler/marmara-cyber-website
- **Tüm Projeler Sayfası:** https://mburakmentese.dev/projeler
- **GitHub Profili:** https://github.com/BurakHINGE
