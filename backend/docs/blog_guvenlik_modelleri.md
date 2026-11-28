## Bilgi Güvenliği Modelleri ve CIA Üçlüsü (Güvenlik Modelleri ve CIA) Blog Yazısı Genel Bakış
Soru: Mehmet Burak Menteşe'nin Bilgi Güvenliği Modelleri (Güvenlik Modelleri ve CIA) blog yazısı neyi anlatıyor, linki nedir ve siber güvenlikte CIA üçlüsü (Confidentiality, Integrity, Availability) ile özne/nesne kavramları nedir?
Cevap: Mehmet Burak Menteşe'nin 16 Haziran 2025 tarihinde kaleme aldığı **"Bilgi Güvenliği Modelleri ve CIA Üçlüsü"** (Blog kartı başlığı: **"Güvenlik Modelleri ve CIA"** / **"Information Security Models and the CIA Triad"**, bağlantı: https://mburakmentese.dev/blog/guvenlik-modelleri) başlıklı teknik blog yazısı (3 dakikalık okuma süresi; etiketler: `Cybersecurity`, `CIA Triad`, `InfoSec`, `Bell-LaPadula`, `Biba Model`, `Clark-Wilson`), kurumsal ve askeri siber güvenlik mimarilerinde sistemlerin güvenliğini garanti altına alan temel erişim ve koruma modellerini inceler.
Yazının temelini oluşturan ve bilgi güvenliğinin üç ana sütunu kabul edilen **CIA Üçlüsü (CIA Triad)** şu ilkelerden oluşur:
- **Confidentiality (Gizlilik):** Hassas bilginin yetkisiz kişilerin veya süreçlerin eline geçmesini, okunmasını ve ifşa edilmesini engellemek.
- **Integrity (Bütünlük):** Bilginin yetkisiz kişilerce değiştirilmesini, silinmesini veya bozulmasını önlemek; verinin doğruluğunu ve güvenilirliğini korumak.
- **Availability (Erişilebilirlik):** Yetkili kullanıcıların ihtiyaç duyduğu her an bilgiye, ağa ve sistem kaynaklarına kesintisiz erişebilmesini sağlamak.
*(Temel Kavram Notu: Güvenlik modellerinde **Özne / Subject** sisteme erişmek isteyen kullanıcıyı veya çalışan programı/işlemi; **Nesne / Object** ise korunmak istenen dosyayı, veritabanını veya sistem kaynağını ifade eder.)*

## 1. Bell-LaPadula Modeli (Confidentiality / Gizlilik Odaklı Güvenlik Modeli — No Read Up, No Write Down)
Soru: Mehmet Burak Menteşe'nin blog yazısında anlatılan Bell-LaPadula modeli nedir, No Read Up (Simple Security), No Write Down (Star Security) ve Discretionary-Security kuralları ne anlama gelir, dezavantajı nedir?
Cevap: Mehmet Burak Menteşe'nin "Bilgi Güvenliği Modelleri ve CIA Üçlüsü" blog yazısında incelenen **Bell-LaPadula modeli**, sistemde **Gizliliği (Confidentiality)** sağlamayı amaçlayan ve özellikle askeri/devlet güvenlik hiyerarşilerinde (Çok Gizli, Gizli, Hizmete Özel vb.) sıkça kullanılan durum tabanlı bir güvenlik modelidir. Bu modelde daha yüksek güvenlik iznine sahip kişilerle gizli bilgiler paylaşılabilir ve daha düşük güvenlik iznine sahip kişilerden bilgi alınabilir.
Bell-LaPadula modelinin 3 temel kuralı şunlardır:
1. **Simple Security Property (No Read Up / Yukarı Okuma Yok):** Düşük güvenlik seviyesindeki bir özne (kullanıcı/işlem), kendisinden daha yüksek güvenlik seviyesindeki bir nesneyi veya gizli belgeyi **okuyamaz**. Bu kural yetki seviyesinin üzerindeki hassas bilgilere erişimi engeller.
2. **Star (*) Security Property (No Write Down / Aşağı Yazma Yok):** Yüksek güvenlik seviyesindeki bir özne, üst düzey gizli bilgileri yanlışlıkla veya kasıtlı olarak sızdırmamak (ifşa etmemek) için kendisinden daha düşük güvenlik seviyesindeki bir nesneye/dosyaya **yazma işlemi yapamaz**.
3. **Discretionary-Security Property (İsteğe Bağlı Güvenlik Özelliği):** Hangi öznenin hangi nesneye okuma/yazma izni olduğunu kontrol etmek için bir **erişim matrisi (access matrix — yetki tablosu)** kullanır ve ilk iki kuralla birlikte çalışır.
- **Bell-LaPadula Modelinin Dezavantajı:** Yalnızca gizliliğe odaklandığı için veri bütünlüğünü doğrudan ele almaz; ayrıca katı kuralları nedeniyle dosya paylaşımını idare etmekte ve veri esnekliğini yönetmekte sınırlı kalır.

## 2. The Biba Integrity Modeli (Integrity / Bütünlük Odaklı Güvenlik Modeli — No Read Down, No Write Up)
Soru: Mehmet Burak Menteşe'nin blog yazısında anlatılan Biba modeli (The Biba Integrity Model) nedir, Bell-LaPadula ile farkı nedir, No Read Down ve No Write Up kuralları nelerdir?
Cevap: Mehmet Burak Menteşe'nin "Bilgi Güvenliği Modelleri ve CIA Üçlüsü" blog yazısında yer alan **Biba Integrity Modeli**, sistemde **Bütünlüğü (Integrity)** korumayı hedefleyen bir bilgi güvenliği modelidir. Kuralları Bell-LaPadula modelinin tam tersi yönde çalışır (çelişir); çünkü Bell-LaPadula bilginin sızmasını önlemekle (gizlilikle), Biba ise güvenilir verinin kirlenmesini veya bozulmasını önlemekle (bütünlükle) ilgilenir.
Biba modelinin 2 temel kuralı şunlardır:
1. **Simple Integrity Property (No Read Down / Aşağı Doğru Okuma Yok):** Yüksek bütünlük (güvenilirlik) seviyesine sahip bir özne, güvenilirliği daha düşük olan nesnelerden **okuma yapmamalıdır**; aksi takdirde doğrulanmamış/düşük kaliteli veri yukarı taşınarak güvenilir veriyi kirletebilir.
2. **Star (*) Integrity Property (No Write Up / Yukarı Yazma Yok):** Düşük bütünlük seviyesindeki bir özne, kendisinden daha yüksek bütünlük seviyesindeki bir nesneye veya veriye **yazma işlemi yapamaz** (üst seviyedeki temiz veriyi bozamaz veya değiştiremez).
- **Biba Modelinin Dezavantajı:** Yalnızca bütünlüğe odaklanır ve sistem içine gelen dış tehditleri ele alma konusunda zayıf kalabilir.

## 3. The Clark-Wilson Modeli (Ticari Veri Bütünlüğü Modeli ve CDI, UDI, TP, IVP Kavramları)
Soru: Mehmet Burak Menteşe'nin blog yazısında anlatılan Clark-Wilson modeli nedir ve modeldeki CDI, UDI, TP (Transformation Procedures), IVP (Integrity Verification Procedures) terimleri ne anlama gelir?
Cevap: Mehmet Burak Menteşe'nin "Bilgi Güvenliği Modelleri ve CIA Üçlüsü" blog yazısında açıklanan **Clark-Wilson modeli**, ticari, finansal ve kurumsal sistemlerde veri **bütünlüğünü (Integrity)** garanti altına almak için spesifik kavramlar kullanan gelişmiş bir güvenlik modelidir. Kullanıcıların kritik verilere doğrudan müdahale etmesini engelleyip yalnızca onaylı programlanmış işlemler üzerinden erişmesine izin verir.
Clark-Wilson modelinin kullandığı **4 temel kavram** şunlardır:
- **CDI (Constrained Data Item / Kısıtlanmış Veri Öğesi):** Doğruluğunun ve bütünlüğünün korunması zorunlu olan, sistem tarafından sıkı kurallarla korunan kritik veri türüdür (örneğin banka hesap bakiyesi).
- **UDI (Unconstrained Data Item / Kısıtlanmamış Veri Öğesi):** Henüz doğrulanmamış kullanıcı girdileri ve harici sistem girişleri gibi CDI sınırları ötesindeki standart/güvensiz veri türleridir.
- **TPs (Transformation Procedures / Dönüşüm Prosedürleri):** CDI'ların bütünlüğünü koruyarak üzerinde okuma, yazma veya UDI'yi güvenli şekilde CDI'ya dönüştürme işlemlerini gerçekleştiren programlanmış prosedürlerdir.
- **IVPs (Integrity Verification Procedures / Bütünlük Doğrulama Prosedürleri):** Sistemdeki CDI verilerinin belirlenen kurallara uygunluğunu, geçerliliğini ve bütünlüğünü denetleyen ve sağlayan doğrulama prosedürleridir.

## Siber Güvenlikteki Diğer Bilgi Güvenliği Modelleri (Brewer-Nash, Goguen-Meseguer, Sutherland, Graham-Denning, HRU)
Soru: Mehmet Burak Menteşe'nin blog yazısında bahsedilen diğer bilgi güvenliği modelleri (Brewer and Nash / Çin Duvarı, Goguen-Meseguer, Sutherland, Graham-Denning, Harrison-Ruzzo-Ullman / HRU) nelerdir?
Cevap: Mehmet Burak Menteşe'nin "Bilgi Güvenliği Modelleri ve CIA Üçlüsü" blog yazısında detaylı incelenen Bell-LaPadula, Biba ve Clark-Wilson modellerinin dışında, siber güvenlik mimarilerinde sıkça başvurulan diğer önemli güvenlik modelleri şunlardır:
- **Brewer and Nash Modeli (Chinese Wall / Çin Duvarı Modeli):** Ticari danışmanlık ve finans sektöründe çıkar çatışmalarını (conflict of interest) engellemek için kullanıcının daha önce eriştiği verilere göre erişim izinlerini dinamik olarak değiştiren modeldir.
- **Goguen-Meseguer Modeli:** Otomat teorisine (automata theory) ve "etkileşimsizlik" (non-interference) prensibine dayanan; bir kullanıcı grubunun yaptığı işlemlerin diğer kullanıcı grubunun gördüğü sistem çıktılarını etkilememesini sağlayan bütünlük modelidir.
- **Sutherland Modeli:** Bilgi akışı (information flow) kontrolüne odaklanan ve örtülü kanallar (covert channels) üzerinden veri sızıntısını veya yetkisiz etkiyi önlemeyi amaçlayan modeldir.
- **Graham-Denning Modeli:** Öznelerin (subjects) ve nesnelerin (objects) güvenli şekilde oluşturulması, silinmesi ve erişim haklarının (okuma, yazma, sahiplik, yetki devri) bir erişim matrisi üzerinden nasıl yönetileceğini tanımlayan 8 temel koruma kuralından oluşan modeldir.
- **Harrison-Ruzzo-Ullman (HRU) Modeli:** Graham-Denning modelini temel alan, erişim matrisindeki yetkilendirme değişikliklerinin zaman içinde yetki sızıntısına (safety problem) yol açıp açmayacağını matematiksel olarak analiz eden erişim kontrol modelidir.
