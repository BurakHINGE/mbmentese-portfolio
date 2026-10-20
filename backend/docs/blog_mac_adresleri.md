## MAC Adresi ve ARP Blog Yazısı Genel Bakış ve Yayımlanma Süreci
Soru: Mehmet Burak Menteşe'nin MAC Adresi ve ARP (MAC Address and ARP) blog yazısı neyi anlatıyor, ne zaman ve nerede yayımlandı?
Cevap: Mehmet Burak Menteşe'nin 16 Ağustos 2025 tarihinde kaleme aldığı **"MAC Adresi ve ARP: Cihazlar Nasıl İletişim Kurar?"** (İngilizce: **"MAC Address and ARP: How Do Devices Communicate?"**) başlıklı teknik blog makalesi, orijinal olarak **Marmara Üniversitesi Siber Güvenlik Kulübü (MÜSİBER / Marmara Siber)** çatısı altında yazılmış ve Medium'daki resmi kulüp yayınında editör onayından geçerek yayımlanmıştır; ayrıca portfolyo sitesinde (`https://mburakmentese.dev/blog/mac-adresi-ve-arp`) yer almaktadır.
8 dakikalık okuma süresine sahip olan makale (Etiketler: `Network`, `ARP Protocol`, `OSI Layers`, `Cybersecurity`, `MAC Address`, `Private IP`); bilgisayarların yerel ağda (LAN) birbirini nasıl bulduğunu, veri iletim süreçlerini, OSI katmanlarını, NIC (Ağ Kartı) donanımını, Private/Public IP farklarını ve ARP protokolünün işleyişini sade ve anlaşılır bir dille anlatır.

## Temel Kavram: NIC (Network Interface Card / Ağ Arayüz Kartı) Nedir ve Cihazlarda Kaç Adet Bulunur?
Soru: NIC (Ağ Arayüz Kartı / Network Interface Card) nedir, görevleri nelerdir, bilgisayarlarda ve telefonlarda kaç tane NIC ve MAC adresi bulunur?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında açıklandığı üzere; **NIC (Network Interface Card / Ağ Arayüz Kartı)**, bir cihazın internete ve yerel ağa bağlanmasını sağlayan temel donanım bileşenidir. Ağdan gelen fiziksel sinyalleri (elektrik veya radyo dalgalarını) cihazın anlayacağı dijital verilere (bitlere) çevirir ve cihaz içindeki verileri ağa gönderir. En kritik özelliği, üretici tarafından donanıma işlenmiş olan fiziksel **MAC adresini** barındırmasıdır:
- **Bilgisayarlarda ve Sunucularda NIC Sayısı:** Tipik bir bilgisayarda **Ethernet (kablolu), Wi-Fi (kablosuz) ve Bluetooth** için 1'er tane olmak üzere **en az 3 adet NIC** (dolayısıyla 3 ayrı MAC adresi) bulunabilir; sunucularda (server) bu sayı çok daha fazla olabilir.
- **Akıllı Telefonlarda NIC Sayısı ve 4G/5G Şebekeleri:** Akıllı telefonlarda dahili Ethernet portu bulunmadığı için genellikle **en fazla 2 adet MAC adresi (Wi-Fi ve Bluetooth)** yer alır. 4G ve 5G mobil hücresel şebekelerde MAC adresi doğrudan kullanılmaz; cihaz kimliği için SIM kart ve hücresel şebekeyle ilişkili kimlikler (IMEI/IMSI vb.) kullanılır.

## OSI Referans Modeli ve MAC Adresinin Bulunduğu 2. Katman (Data Link Layer)
Soru: MAC adresi OSI modelinin hangi katmanında çalışır, Veri Bağlantısı (Data Link) katmanının görevi nedir ve 1., 2., 3. katmanlar nasıl etkileşir?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında anlatıldığı üzere; **MAC adresi, OSI (Open Systems Interconnection) referans modelinin 2. katmanı olan Veri Bağlantısı (Data Link) katmanında** yer alır. OSI modelinin alt katmanları (1-4) verinin ağ üzerinde taşınması ve iletilmesinden, üst katmanları (5-7) ise verinin uygulama düzeyinde hazırlanması ve sunulmasından sorumludur:
- **1. Katman (Fiziksel Katman / Physical Layer):** NIC donanımı bu katmanda fiziksel sinyalleri 0 ve 1'lerden oluşan bitlere çevirir.
- **2. Katman (Veri Bağlantısı Katmanı / Data Link Layer):** *"Bu veri yerel ağda (LAN) fiziksel olarak kime gidecek?"* sorusuna yanıt verir ve hedef cihazın **MAC adresini** kullanarak çerçeve (frame) yönlendirmesi yapar.
- **3. Katman (Ağ Katmanı / Network Layer):** Mantıksal **IP adresi** ve ağlar arası yönlendirme (routing) ile ilgilenir; yerel ağ içi teslimat için 2. katmandaki MAC adresiyle entegre çalışır.

## MAC Adresi Nedir, Yapısı Nasıldır (48 Bit, Hexadecimal, OUI) ve MAC Spoofing Nedir?
Soru: MAC adresi (Media Access Control) nedir, kaç bitten oluşur, OUI kodu nedir ve MAC adresi değiştirilebilir mi (MAC Spoofing)?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında tanımlandığı üzere; **MAC (Media Access Control) adresi**, ağa bağlanan her ağ kartının (NIC) fiziksel kimlik kartıdır. Fabrikada üretim sırasında donanımsal olarak atanır ve fiziksel olarak kalıcıdır (ancak yazılımsal olarak işletim sistemi düzeyinde taklit edilebilir; buna **MAC Spoofing / MAC Taklidi** denir).
MAC adresinin temel özellikleri ve yapısı şunlardır:
- **48 Bit ve 12 Hexadecimal Karakter:** Toplam **48 bitten (6 byte)** oluşur ve iki nokta veya tire ile ayrılmış **12 onaltılık (hexadecimal)** karakter halinde gösterilir (Örnek: `A4:BC:12:DE:34:56`).
- **OUI (Organizationally Unique Identifier / Üretici Kodu):** MAC adresinin **ilk 6 hanesi (ilk 24 bit)** donanımı üreten firmayı (Intel, Apple, TP-Link vb.) temsil eden benzersiz **OUI** kodudur; **son 6 hanesi (son 24 bit)** ise üretici tarafından o ağ kartına verilen benzersiz seri numarasıdır.
- **Yerel Ağ (LAN) Sınırı:** MAC adresleri cihazların birbirini tanımasını ve doğrudan haberleşmesini **yalnızca aynı yerel ağ (LAN)** içinde gerçekleştirebilir. Cihaz farklı bir ağa taşınsa bile fiziksel MAC adresi sabit kalır.

## Public IP, Private IP ve MAC Adresi Arasındaki Farklar
Soru: MAC adresi ile IP adresi (Public IP ve Private IP) arasındaki temel farklar nelerdir, neden ikisine birden ihtiyaç duyulur?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında karşılaştırıldığı üzere; ağ iletişiminde MAC adresi ve IP adresi birbirini tamamlayan iki farklı adresleme katmanıdır:
- **Private IP (Özel / Yerel IP):** Yerel ağdaki (LAN — örneğin ev veya ofis ağı) her cihaza modem/router (DHCP) tarafından atanan ve yalnızca o iç ağda geçerli olan mantıksal adrestir (Örn: `192.168.1.12`).
- **Public IP (Genel / Dış IP):** O yerel ağın dış internete açılırken kullandığı, internet servis sağlayıcısı (ISS) tarafından atanan tek ve genel IP adresidir.
- **MAC Adresi vs IP Adresi Farkı:** **MAC adresi** cihazın değişmeyen **"fiziksel kimliği"**dir ve yalnızca aynı yerel ağ (LAN) içindeki cihazların birbirini bulmasını sağlar. **IP adresi** ise cihazın bağlı olduğu ağa göre değişebilen **"mantıksal konumu/adresi"**dir ve verinin bir yerel ağdan dış ağlara veya internete çıkarken yönlendirilmesi (routing) için kullanılır. Kısaca; MAC adresi kimliktir, IP adresi ise bulunulan adrestir.

## ARP (Address Resolution Protocol) Nedir, Nasıl Çalışır, ARP Cache, NDP ve ARP Spoofing Nedir?
Soru: ARP (Adres Çözümleme Protokolü) nedir ve nasıl çalışır? ARP Cache, IPv6 NDP ve ARP Spoofing (ARP Zehirlenmesi) ne anlama gelir?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında detaylıca anlatıldığı üzere; bilgisayarlar yerel ağda bir cihaza veri göndermek istediklerinde hedef cihazın **IP adresini** bilirler ancak veriyi 2. katmanda fiziksel olarak iletebilmek için hedef cihazın **MAC adresine** ihtiyaç duyarlar. Yerel ağda bilinen IP adresini MAC adresine çeviren köprü protokolü **ARP (Address Resolution Protocol / Adres Çözümleme Protokolü)**'dür.
ARP protokolünün 3 adımda çalışma mantığı:
1. **ARP Request (Broadcast / Genel Yayın):** Kaynak cihaz yerel ağdaki tüm cihazlara açık bir yayın (Broadcast) göndererek sorar: *"Hey, `192.168.1.12` IP adresi kimde? Bana MAC adresini söylesin!"*
2. **ARP Reply (Unicast / Tekil Yanıt):** Yalnızca ilgili IP adresine sahip olan hedef cihaz kaynağa doğrudan tekil (Unicast) cevap döner: *"Bu IP benim! MAC adresim: `A4:BC:12:DE:34:56`"*
3. **ARP Cache (ARP Tablosu):** Kaynak bilgisayar bu IP-MAC eşleşmesini saliseler içinde öğrenir ve her paket için tekrar ağa sormamak adına geçici önbelleği olan **ARP Cache (ARP Tablosu)** içine kaydeder.
- **IPv4 vs IPv6 (NDP):** ARP protokolü yalnızca **IPv4** ağları için geçerlidir. **IPv6** ağlarında ARP yerine **NDP (Neighbor Discovery Protocol / Komşu Keşif Protokolü)** kullanılır.
- **ARP Spoofing (ARP Zehirlenmesi):** ARP protokolünde kimlik doğrulama mekanizması bulunmadığı için, yerel ağdaki bir saldırganın sahte ARP yanıtları göndererek hedef cihazların ARP tablosunu kandırması ve ağ trafiğini kendi üzerinden geçirmesi (Ortadaki Adam / MITM saldırısı) yöntemine **ARP Spoofing** denir.

## Veri İletişiminde Switch (Anahtar) ve Router (Yönlendirici) Nasıl Çalışır?
Soru: Yerel ağda ve internete çıkarken veri gönderiminde Switch ve Router nasıl çalışır, OSI'nin hangi katmanında görev yaparlar?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında açıklandığı üzere; bir veri paketinin yolculuğunda **Switch** ve **Router** farklı OSI katmanlarında görev yapar:
- **Switch (Anahtar — OSI 2. Katman):** Cihazdan çıkan veri önce yerel ağdaki Switch'e ulaşır. Switch **2. katmanda (Data Link)** çalışır ve gelen çerçevedeki hedef **MAC adresini** okur. Kendi MAC adres tablosu (CAM tablosu) sayesinde ağdaki hangi MAC adresinin hangi fiziksel porta bağlı olduğunu bilir ve paketi tüm ağa yaymak yerine yalnızca hedef cihaza giden porta iletir.
- **Router (Yönlendirici — OSI 3. Katman):** Eğer paket yerel ağın (LAN) dışına, yani internete veya başka bir ağa çıkacaksa varsayılan ağ geçidi olan Router'a gönderilir. Router paketin 2. katman başlığını ve MAC adresini kontrol eder; hedef MAC adresi Router'ın kendisine aitse paketin yerel ağ sınırını geçmek istediğini anlar. Veriyi **3. katmana (Ağ / IP Katmanı)** çıkarır, 2. katman MAC başlığını soyar ve hedef **IP adresine** göre internete giden en uygun rotayı hesaplayarak paketi bir sonraki düğüme yönlendirir.

## MAC Katmanı Protokolleri (Ethernet, IEEE 802.11, CSMA/CD, WAN) ve Erişim Algoritmaları
Soru: MAC katmanında çalışan protokoller (Ethernet, IEEE 802.11, CSMA/CD, PPP, HDLC) ve ortam erişim algoritmaları (Contention-Based ve Controlled Access) nelerdir?
Cevap: Mehmet Burak Menteşe'nin "MAC Adresi ve ARP" blog yazısında incelenen 2. katman protokolleri ve erişim yöntemleri şunlardır:
- **MAC Katmanı Protokolleri:**
  1. **Ethernet (IEEE 802.3):** Kablolu yerel ağlarda (LAN) çerçeve yapısını ve kaynak/hedef MAC başlıklarını taşıyan en yaygın standart protokoldür.
  2. **IEEE 802.11 (Wi-Fi):** Kablosuz yerel ağlarda (WLAN) 2. katmanda çalışan ve kablosuz sinyal üzerinden MAC adres bilgilerini taşıyan standarttır.
  3. **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):** Eski paylaşımlı kablolu ağlarda (Hub dönemlerinde) iki cihaz aynı anda veri gönderdiğinde oluşan sinyal çakışmasını (collision) algılayan yöntemdir; günümüzde aynı anda hem veri gönderip hem alabilen **full-duplex (tam çift yönlü) Switch'ler** sayesinde kablolu ağlarda çakışma kalmadığı için tarihsel/teorik bir bilgi olarak kalmıştır.
  4. **PPP, HDLC ve Frame Relay:** Noktadan noktaya (point-to-point) veya **WAN (Wide Area Network / Geniş Alan Ağı)** bağlantılarında kullanılan 2. katman protokolleridir; yerel ağ (LAN) yayın ortamı olmadıkları için Ethernet tipi MAC adresi taşımazlar.
- **MAC Ortam Erişim Algoritmaları:**
  1. **Contention-Based (Rekabete Dayalı) MAC:** Cihazlar ortak iletişim hattının boş olup olmadığını kontrol eder; hat boşsa veri yollar, iki cihaz aynı anda gönderip çakışma (collision) yaşanırsa rastgele bir süre (backoff) bekleyip yeniden dener (Ethernet ve Wi-Fi bu mantığa dayanır).
  2. **Controlled Access (Kontrollü Erişim) MAC:** Cihazların veri gönderme sırası (token/jeton veya zaman dilimi ile) önceden merkezi veya sıralı olarak belirlenir; böylece cihazlar sırayla konuştuğu için veri çakışması tamamen önlenir.
