## Marmara Siber Web Arayüzü (Marmara Cyber Web Sitesi) Yapılış Amacı ve Hedef Kitlesi
Soru: Mehmet Burak Menteşe tarafından geliştirilen Marmara Siber Web Arayüzü (Marmara Cyber Web Interface / marmaracyber.com) neden yapıldı, amacı ve hedef kitlesi nedir?
Cevap: Mehmet Burak Menteşe'nin Akademi Komitesi Başkanı olarak sıfırdan geliştirdiği Marmara Siber Web Arayüzü (`https://marmaracyber.com`), Marmara Üniversitesi'ne yeni kayıt olan öğrenciler başta olmak üzere kulüp ve siber güvenlik alanı hakkında bilgi edinmek isteyen herkes için hazırlanmıştır. Temel amacı **Marmara Üniversitesi Siber Güvenlik Kulübü (MÜSİBER / Marmara Siber)** hakkında detaylı bilgi sunmak, topluluğu tanıtmak ve kulübün gerçekleştirdiği etkinlikler, atölyeler ve eğitimler hakkında çalışmaların biriktirildiği kurumsal bir dijital portfolyo görevi görmektir.

## Marmara Siber Web Sitesinin Bölümleri, Ekip Şeması ve İletişim Kanalları
Soru: Mehmet Burak Menteşe'nin geliştirdiği Marmara Siber (Marmara Cyber) web sitesinde hangi bölümler yer alıyor, kulüp ekibiyle nasıl iletişime geçilir?
Cevap: Mehmet Burak Menteşe'nin tasarladığı Marmara Siber web sitesinde (`marmaracyber.com`) şu ana bölümler yer almaktadır:
- **Hakkımızda ve Etkinlikler:** Kulübün vizyonunu, teknik atölyelerini ve siber güvenlik çalışmalarını tanıtan bölüm.
- **Ekibimiz (Hiyerarşik Ekip Şeması):** Yönetim kurulu ve komite başkanlarının (Akademi Komitesi Başkanı Mehmet Burak Menteşe dahil) görevlerinin ve LinkedIn, Instagram gibi sosyal medya hesaplarının yer aldığı hiyerarşik ekip bölümü; ziyaretçiler buradan ekip üyeleriyle doğrudan iletişime geçebilir.
- **Dinamik SSS (Sıkça Sorulan Sorular / Akordiyon S.S.S. / Accordion UI):** Öğrencilerin siber güvenlik, yazılım geçmişi, İngilizce ve kulüp ortamı hakkındaki sorularını yanıtlayan açılır-kapanır akordeon menü bölümü.
- **Bizimle İletişime Geçin (Contact Us):** Ziyaretçilerden dinamik olarak veri (input) alan, girdi sanitizasyonu (XSS koruması) ve honeypot ile Formspree üzerinden güvenli şekilde çalışan interaktif iletişim/başvuru formu.

## Marmara Siber Web Arayüzü Projesinde Neden Vanilla JavaScript Tercih Edildi?
Soru: Mehmet Burak Menteşe, Marmara Siber Web Arayüzü (Marmara Cyber) sitesinde React veya Vue gibi kütüphaneler yerine neden Vanilla JS kullandı?
Cevap: Mehmet Burak Menteşe, Marmara Siber web sitesinin (`marmaracyber.com`) tamamen hafif, sade, hızlı açılan, statik barındırmaya tam uyumlu ve gereksiz paket bağımlılıklarından (dependency) uzak bir yapıda olmasını istediği için saf **Vanilla JavaScript** tercih etmiştir. Bu sayede React veya Vue gibi harici bir framework yükü olmadan; DOM manipülasyonu, akordeon SSS menüleri ve sayfa yenilenmeden çalışan anahtar-değer (key-value) tabanlı TR/EN (`i18n`) dil çeviri motoru yüksek hız ve yalın bir mimariyle elde edilmiştir.

## Marmara Siber Web Arayüzü Geliştirilirken Karşılaşılan En Büyük Teknik Zorluk (Responsive Tasarım, Flexbox ve Grid)
Soru: Marmara Siber Web Arayüzü (Marmara Cyber) sitesi geliştirilirken Mehmet Burak Menteşe'nin karşılaştığı en büyük teknik zorluk neydi ve nasıl çözüldü?
Cevap: Mehmet Burak Menteşe'nin geliştirme sürecinde karşılaştığı en büyük teknik zorluk, fütüristik siberpunk cam efektli (glassmorphism) arayüzün ve hiyerarşik yönetim kartlarının mobil telefon, tablet ve masaüstü gibi farklı ekran boyutlarına sahip cihazlara kusursuz uyum sağlaması (**responsive adaptasyon**) olmuştur. Bu sorun, **CSS Flexbox** ve **CSS Grid** yerleşim sistemleri ile medya sorguları (`@media queries`) kullanılarak çözülmüştür:
- **CSS Flexbox (Esnek Kutu Yerleşimi):** Sayfa içindeki butonların, menü öğelerinin ve kart içeriklerinin tek boyutta (satır veya sütun olarak) ekran genişliğine göre esnek biçimde hizalanmasını sağlar.
- **CSS Grid (Izgara Yerleşimi):** Ekip kartları ve proje bölmeleri gibi çok sütunlu yapıların iki boyutlu (hem satır hem sütun) ızgara sistemiyle masaüstünde yan yana, mobil ekranlarda ise otomatik olarak dikey akışta alt alta dizilmesini sağlar.

## Marmara Siber Web Sitesinin Canlı Adresi ve Yayını
Soru: Mehmet Burak Menteşe'nin geliştirdiği Marmara Siber Web Arayüzü (Marmara Cyber) web sitesine nasıl erişebilirim, güncel linki nedir?
Cevap: Mehmet Burak Menteşe tarafından geliştirilen Marmara Üniversitesi Siber Güvenlik Kulübü (MÜSİBER) resmi web sitesi aktif olarak yayındadır ve doğrudan https://marmaracyber.com/ adresi üzerinden ziyaret edilebilir. Projenin portfolyodaki detaylı incelemesine https://mburakmentese.dev/projeler/marmara-cyber-website ve tüm projeler listesine https://mburakmentese.dev/projeler sayfasından ulaşılabilir.
