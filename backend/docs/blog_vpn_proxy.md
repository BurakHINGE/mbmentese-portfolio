## VPN ve Proxy Kavramları Blog Yazısı Genel Bakış ve Kapsamı
Soru: Mehmet Burak Menteşe'nin VPN ve Proxy Kavramları (VPN and Proxy Concepts) blog yazısı neyi anlatıyor, ne zaman yazıldı ve kapsamı nedir?
Cevap: Mehmet Burak Menteşe'nin 19 Mayıs 2025 tarihinde kaleme aldığı **"VPN ve Proxy Kavramları"** (İngilizce: **"VPN and Proxy Concepts"**, bağlantı: `https://mburakmentese.dev/blog/vpn-ve-proxy-kavramlari`) başlıklı teknik blog yazısı (2 dakikalık okuma süresi, Etiketler: `Network`, `VPN`, `Proxy`, `Privacy`, `Architecture`); internet ve siber güvenlik dünyasında sıkça birbiriyle karıştırılan **VPN (Virtual Private Network)** ve **Proxy (Vekil Sunucu)** servislerinin ortak noktalarını, çalışma prensiplerini, şifreleme/kapsam farklarını ve güvenlik düzeylerini sade bir dille inceler.

## VPN (Sanal Özel Ağ / Virtual Private Network) Nedir, Nasıl Çalışır ve Tünelleme (Tunneling) Ne Anlama Gelir?
Soru: VPN (Virtual Private Network / Sanal Özel Ağ) nedir, nasıl çalışır, Tünelleme (Tunneling) ve İSS (ISP) koruması ne anlama gelir?
Cevap: Mehmet Burak Menteşe'nin "VPN ve Proxy Kavramları" blog yazısında açıklandığı üzere; **VPN (Virtual Private Network / Sanal Özel Ağ)**, kullanıcı cihazı ile hedef VPN sunucusu arasındaki veri iletişiminin uçtan uca güçlü kriptografik algoritmalarla şifrelendiği bir ağ güvenlik servisidir.
- **Tünelleme (Tunneling) Nedir?** Verilerin açık internet ağı üzerinden geçerken dışarıdan hiç kimsenin okuyamayacağı şifrelenmiş özel bir sanal veri hattı (koridor) içinden taşınmasına **"Tünel" (Tunneling)** adı verilir.
- **VPN'in Temel Özellikleri:**
  1. **Uçtan Uca Şifreleme (Encrypted Connection):** Veri trafiği kullanıcı cihazından çıktığı andan VPN sunucusuna ulaşana kadar tamamen şifrelidir.
  2. **İSS (ISP) ve Ortadaki Adam Koruması:** **İnternet Servis Sağlayıcıları (İSS / ISP — kullanıcıya internet hizmeti veren telekom şirketleri)**, kamuya açık (kafe, havaalanı vb.) Wi-Fi yöneticileri veya ağdaki üçüncü şahıslar gönderilen ve alınan verileri kesinlikle okuyamaz ve izleyemez.
  3. **Tüm İşletim Sistemi Kapsamı:** Cihazdaki yalnızca web tarayıcısını değil, arka planda çalışan tüm masaüstü/mobil uygulamaların ve sistem servislerinin internet trafiğini (tüm işletim sistemini) eksiksiz kapsar.
  4. **Yüksek Gizlilik:** Yüksek düzeyde veri güvenliği ve mahremiyet sağlar.

## Proxy (Vekil Sunucu) Nedir, Nasıl Çalışır ve Neden Tam Güvenlik Sağlamaz?
Soru: Proxy (Vekil Sunucu) nedir, nasıl çalışır ve siber güvenlik açısından neden VPN kadar güvenli değildir?
Cevap: Mehmet Burak Menteşe'nin "VPN ve Proxy Kavramları" blog yazısında tanımlandığı üzere; **Proxy (Vekil Sunucu)**, kullanıcının çevrimiçi bir web kaynağına erişirken kendi cihazı ile hedef site arasında aracı (vekil) olarak kullandığı bir sunucu servisidir. Temel işlevi veriyi şifrelemek değil, yalnızca internet trafiğine aracılık ederek IP adresini maskelemektir.
- **Proxy'nin Temel Özellikleri ve Güvenlik Sınırları:**
  1. **Şifresiz İletişim (Unencrypted Connection):** Proxy trafiği varsayılan olarak **şifresizdir**; uçtan uca güçlü bir kriptografik anonimlik ve gizlilik sağlamaz.
  2. **İSS (ISP) Tarafından İzlenebilirlik:** Proxy sunucusuna güvenlik taahhüdü verilse bile sunucuya giden şifresiz trafik, İnternet Servis Sağlayıcıları (İSS / ISP) veya yerel ağdaki üçüncü şahıslar tarafından okunabilir ve izlenebilir.
  3. **Sınırlı Kapsam (Uygulama Bazlı):** Tüm işletim sistemini değil, yalnızca yapılandırılan web tarayıcısını veya belirli tek bir yazılımı kapsar.
  4. **Hız vs Güvenlik Dengesi:** Ağır bir şifreleme yükü olmadığı için VPN'e kıyasla daha hızlı çalışabilir ancak siber güvenlik ve veri gizliliği açısından savunmasızdır.

## VPN ve Proxy Servislerinin 3 Temel Ortak Noktası (IP Gizleme, Loglama, Geo-blocking)
Soru: VPN ve Proxy servislerinin ortak noktaları nelerdir? Loglama (Logging), Monitoring ve Geo-blocking (Coğrafi Kısıtlama) ne demektir?
Cevap: Mehmet Burak Menteşe'nin "VPN ve Proxy Kavramları" blog yazısında belirtildiği üzere, VPN ve Proxy servislerinin paylaştığı **3 temel ortak özellik** şunlardır:
1. **IP Adresi Değişikliği (IP Maskeleme):** Her iki servis de kullanıcının gerçek Public IP adresini gizleyerek hedef web sitesine kendi ara sunucusunun IP adresini gösterir.
2. **Loglama (Logging) ve Monitoring (Ağ İzleme):** Hem VPN hem de Proxy sunucuları üzerinde, servis sağlayıcının politikasına bağlı olarak kullanıcı trafiğine ait erişim kayıtları (**log**) tutulabilir ve ağ izlemesi (**monitoring**) yapılabilir.
3. **Coğrafi Kısıtlamaları (Geo-blocking) Aşma:** Kullanıcının bulunduğu ülkeye kapatılmış web sitelerine veya içeriklere (**Geo-blocking**), farklı ülkelerdeki VPN veya Proxy sunucularına bağlanarak erişim sağlanabilir; bölgesel engeller ve sansürler aşılabilir.

## VPN ile Proxy Arasındaki Temel Farklar ve Hangi Durumda Hangisinin Seçileceği
Soru: VPN ile Proxy arasındaki en kritik farklar nelerdir ve hangi durumda VPN, hangi durumda Proxy tercih edilmelidir?
Cevap: Mehmet Burak Menteşe'nin "VPN ve Proxy Kavramları" blog yazısında özetlenen en kritik farklar şunlardır:
- **Şifreleme:** VPN tüm trafiği güçlü bir şifreli tünelle (tunneling) korurken, Proxy iletişimi şifresiz iletir.
- **Kapsam:** VPN işletim sistemindeki tüm internet trafiğini (tüm uygulamaları) yönlendirirken, Proxy genellikle yalnızca tek bir web tarayıcısı veya uygulama düzeyinde çalışır.
- **Gizlilik ve İSS (ISP) Koruması:** VPN veriyi İnternet Servis Sağlayıcısına (İSS / ISP) karşı da okunamaz kılarken, Proxy kullanımında İSS trafiğin içeriğini görebilir.
- **Hız:** Şifreleme yükü bulunmayan Proxy genellikle daha hızlıdır; VPN ise kriptografik şifreleme işlemi nedeniyle hafif bir hız kaybı yaşatabilir.
- **Kullanım Tercihi Özeti:** Halka açık Wi-Fi ağlarında, hassas işlemlerde ve tam veri gizliliği/güvenliği gerektiğinde **VPN**; güvenlik kaygısı olmayan durumlarda yalnızca hızlıca bölgesel bir IP kısıtlamasını aşmak veya tek bir tarayıcı üzerinde işlem yapmak istendiğinde **Proxy** tercih edilir.
