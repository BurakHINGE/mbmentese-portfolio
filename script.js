
// Typewriter Effect for the Domain Highlight
function initTypewriter() {
    const text = "mburakmentese.dev";
    const target = document.getElementById('typewriter-target');
    if (!target) return;
    target.textContent = '';
    let i = 0;
    function type() {
        if (i < text.length) {
            target.textContent += text.charAt(i);
            i++;
            setTimeout(type, 100); // 100ms per character
        }
    }
    // Start typewriter after a short delay (e.g. 500ms after card fade-in)
    setTimeout(type, 500);
}

// Gelişmiş Arka Plan Yıldız Efekti
function createEnhancedStarfield() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    document.body.prepend(canvas);
    
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.zIndex = '-1';
    canvas.style.pointerEvents = 'none';

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    // Fare pozisyonunu takip et
    let mouseX = canvas.width / 2;
    let mouseY = canvas.height / 2;
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // Yıldızları oluştur
    const stars = [];
    const numStars = 150;
    // CSS'indeki renklere uyumlu palet
    const colors = ['#ffffff', '#ffffff', '#00f2fe', '#8f9cae'];

    for (let i = 0; i < numStars; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 1.5 + 0.5,
            baseOpacity: Math.random() * 0.5 + 0.3,
            speedX: (Math.random() - 0.5) * 0.15, // Yavaşça süzülme hızı
            speedY: (Math.random() - 0.5) * 0.15,
            color: colors[Math.floor(Math.random() * colors.length)],
            z: Math.random() * 2 + 0.5 // Derinlik çarpanı (Parallax için)
        });
    }

    const shootingStars = [];
    let isAnimating = true;

    // Sadece görünür olduğunda çalışması için Observer
    const observer = new IntersectionObserver((entries) => {
        // Eğer ekranda herhangi bir section görünüyorsa animasyonu çalıştır
        const isVisible = entries.some(entry => entry.isIntersecting);
        if (isVisible && !isAnimating) {
            isAnimating = true;
            animate();
        } else if (!isVisible && isAnimating) {
            isAnimating = false;
        }
    }, { threshold: 0.05 });

    // Sayfadaki ana bölümleri gözlemle
    document.querySelectorAll('section, main').forEach(el => observer.observe(el));

    function animate() {
        if (!isAnimating) return; // Görünmüyorsa hesaplama yapma (Performans tasarrufu)

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Farenin merkeze olan uzaklığını hesapla
        const targetX = (mouseX - canvas.width / 2) * 0.03;
        const targetY = (mouseY - canvas.height / 2) * 0.03;

        // Normal Yıldızların Çizimi
        stars.forEach(star => {
            // Süzülme hareketi
            star.x += star.speedX;
            star.y += star.speedY;

            // Parallax etkisi (Yıldızın derinliğine göre fareye tepki vermesi)
            const parallaxX = targetX * star.z;
            const parallaxY = targetY * star.z;

            // Ekran dışına çıkan yıldızları diğer taraftan geri sok
            if (star.x < -50) star.x = canvas.width + 50;
            if (star.x > canvas.width + 50) star.x = -50;
            if (star.y < -50) star.y = canvas.height + 50;
            if (star.y > canvas.height + 50) star.y = -50;

            // Yanıp sönme (Twinkle) matematiği
            let currentOpacity = star.baseOpacity + Math.sin(Date.now() * 0.002 * star.z) * 0.4;
            if (currentOpacity < 0.1) currentOpacity = 0.1;
            if (currentOpacity > 1) currentOpacity = 1;
            
            ctx.fillStyle = star.color;
            ctx.globalAlpha = currentOpacity;
            ctx.beginPath();
            ctx.arc(star.x - parallaxX, star.y - parallaxY, star.size, 0, Math.PI * 2);
            ctx.fill();
        });

        ctx.globalAlpha = 1; // Opaklığı sıfırla

        // Kayan Yıldız (Shooting Star) Mantığı
        if (Math.random() < 0.015) { // %1.5 ihtimalle yeni kayan yıldız üret
            shootingStars.push({
                x: Math.random() * canvas.width * 1.5, // Sağdan da gelebilmesi için alanı genişlettik
                y: 0,
                length: Math.random() * 80 + 30,
                speed: Math.random() * 10 + 6,
                opacity: 1
            });
        }

        // Kayan Yıldızların Çizimi
        for (let i = shootingStars.length - 1; i >= 0; i--) {
            let ss = shootingStars[i];
            
            // Kayan yıldız sol aşağı doğru çapraz gider
            ss.x -= ss.speed;
            ss.y += ss.speed;
            ss.opacity -= 0.015; // Yavaşça sönerek kaybolur

            if (ss.opacity <= 0) {
                shootingStars.splice(i, 1);
                continue;
            }

            // Temandaki neon mavi rengi ile iz bırakma
            ctx.strokeStyle = `rgba(0, 242, 254, ${ss.opacity})`;
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(ss.x, ss.y);
            // Kuyruğu hesapla
            ctx.lineTo(ss.x + ss.length, ss.y - ss.length);
            ctx.stroke();
        }

        requestAnimationFrame(animate);
    }
    
    animate();
}

// Kod bloklarını kopyalama işlevi
function copyCode(button) {
    // Butonun bulunduğu terminal header'ını bul
    const header = button.parentElement;
    // Header'dan sonra gelen <pre><code> etiketindeki metni al
    const code = header.nextElementSibling.innerText;
    
    // Panoya kopyala
    navigator.clipboard.writeText(code).then(() => {
        // Butonun görselini 'Kopyalandı' olarak değiştir
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fa-solid fa-check"></i> Copied';
        button.classList.add('copied');
        
        // 2 saniye sonra eski haline döndür
        setTimeout(() => {
            button.innerHTML = originalText;
            button.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Kopyalama başarısız oldu', err);
    });
}

// --- DİL SEÇENEĞİ (TR/EN) İŞLEMLERİ ---

const translations = {
    "tr": {
        "home": "Ana Sayfa",
        "about": "Hakkımda",
        "projects": "Projeler",
        "blog": "Blog",
        "subtitle": "Kişisel Portfolyo ve Blog",
        "title": "Merhaba, ben Mehmet Burak Menteşe",
        "githubGraph": "GitHub Aktiviteleri",
        "featuredTitle": "ÖNE ÇIKANLAR",
        "featuredProjects": "Projeler",
        "featuredBlogs": "Bloglar",
        "ragTitle": "Yerel RAG Asistanı", 
        "ragDesc": "Kişisel belgelerden bilgi çıkaran, harici API kullanmadan tamamen cihazda çalışan CLI tabanlı yapay zeka asistanı.",
        "libraryTitle": "Library Management System",
        "libraryDesc": "Kitapların raflara dizilmesinden genel kütüphane organizasyonuna kadar tüm süreçleri modelleyen, OOP tabanlı Java uygulaması.",
        
        "inspectProject": "Projeyi İncele ➔",
        "ragBlogTitle": "Local RAG Asistanı (Bölüm 1)",
        "ragBlogDesc": "Yapay zeka uydurmalarını engelleyen Local RAG mimarisine giriş; Embeddings işlemleri ve sunucusuz SQLite entegrasyonu.",
        "macBlogTitle": "MAC Adresi ve ARP",
        "macBlogDesc": "Bilgisayarların ağda birbirini nasıl bulduğunu anlatan rehber; OSI katmanları, NIC, Private IP farkları ve ARP protokolü.",
        "startReading": "Okumaya Başla ➔",
        "quickMenu": "Hızlı Menü",
        "followMe": "Beni Takip Edin",
        "footerDesc": "Marmara Üniversitesi Bilgisayar Mühendisliği.<br>Yapay Zeka, Yazılım Geliştirme ve Siber Güvenlik.",
        "allRightsReserved": "© <span id='current-year'>2026</span> Mehmet Burak Menteşe.<br>Tüm Hakları Saklıdır.<br><span class='designed-by'>Designed by MBM</span>"
    },
    "en": {
        "home": "Home",
        "about": "About Me",
        "projects": "Projects",
        "blog": "Blog",
        "subtitle": "Personal Portfolio and Blog",
        "title": "Hello, I'm Mehmet Burak Menteşe",
        "githubGraph": "GitHub Activities",
        "featuredTitle": "FEATURED",
        "featuredProjects": "Projects",
        "featuredBlogs": "Blogs",
        "ragTitle": "Local RAG Assistant",
        "ragDesc": "A CLI-based AI assistant running entirely locally without external APIs, extracting information from personal documents.",
        "libraryTitle": "Library Management System",
        "libraryDesc": "An OOP-based Java application that models all processes, from organizing books on shelves to general library management.",
        
        "inspectProject": "View Project ➔",
        "ragBlogTitle": "Local RAG Assistant (Part 1)",
        "ragBlogDesc": "Introduction to Local RAG architecture preventing AI hallucinations; Embeddings operations and serverless SQLite integration.",
        "macBlogTitle": "MAC Address and ARP",
        "macBlogDesc": "A guide explaining how computers find each other on a network; OSI layers, NIC, Private IP differences, and the ARP protocol.",
        "startReading": "Start Reading ➔",
        "quickMenu": "Quick Links",
        "followMe": "Follow Me",
        "footerDesc": "Marmara University Computer Engineering.<br>Artificial Intelligence, Software Development, and Cyber Security.",
        "allRightsReserved": "© <span id='current-year'>2026</span> Mehmet Burak Menteşe.<br>All Rights Reserved.<br><span class='designed-by'>Designed by MBM</span>"
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // 1. Dil Ayarları (Tek Buton)
    const langBtn = document.getElementById('lang-toggle-btn');
    
    let currentLang = localStorage.getItem('siteLang') || 'tr';
    setLanguage(currentLang);

    if (langBtn) {
        langBtn.addEventListener('click', () => {
            currentLang = currentLang === 'tr' ? 'en' : 'tr';
            setLanguage(currentLang);
            localStorage.setItem('siteLang', currentLang);
        });
    }

    // 2. Typewriter Efekti Başlatma
    initTypewriter();

    // 3. Footer Dinamik Telif Hakkı Yılı
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
});

function setLanguage(lang) {
    const langBtn = document.getElementById('lang-toggle-btn');
    
    // Butonda aktif DİLİ (veya diğer dili) gösterelim.
    // Şık durması için bir dünya ikonu ekliyoruz.
    if (langBtn) {
        langBtn.innerHTML = `<i class="fa-solid fa-globe"></i> ${lang.toUpperCase()}`;
    }

    document.querySelectorAll('[data-translate]').forEach(el => {
        const key = el.getAttribute('data-translate');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key]; 
        }
    });

    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    document.querySelectorAll('.content-tr').forEach(el => {
        el.style.display = lang === 'tr' ? '' : 'none';
    });
    
    document.querySelectorAll('.content-en').forEach(el => {
        el.style.display = lang === 'en' ? '' : 'none';
    });
}

// --- RESİM GALERİSİ (SLIDER) İŞLEMLERİ ---
let slideIndex = 0;

function showSlide(n) {
    const slides = document.querySelectorAll('.slide');
    
    // Eğer o sayfada slider yoksa kodu çalıştırma (Hata vermesini önler)
    if (slides.length === 0) return; 

    // Sınır kontrolleri (Sona gelince başa sar, baştayken sola basınca sona git)
    if (n >= slides.length) { slideIndex = 0; }
    if (n < 0) { slideIndex = slides.length - 1; }

    // Tüm slaytları gizle
    slides.forEach((slide) => {
        slide.classList.remove('active');
    });

    // Sadece aktif olanı göster
    slides[slideIndex].classList.add('active');
}

function moveSlide(n) {
    slideIndex += n;
    showSlide(slideIndex);
}

// Sayfa ilk yüklendiğinde slider varsa birinci resmi aktif et
document.addEventListener('DOMContentLoaded', () => {
    showSlide(0);
});

// --- LIGHTBOX (RESİM BÜYÜTME) İŞLEMLERİ ---
// Slider içindeki çoklu resimler için
function openLightbox() {
    const activeSlide = document.querySelector('.slide.active');
    if (activeSlide) {
        const lightbox = document.getElementById('lightbox-overlay');
        const lightboxImg = document.getElementById('lightbox-img');
        
        if (lightbox && lightboxImg) {
            lightbox.classList.remove('single-image'); // Önceki tekli resim sınıfını temizle
            lightboxImg.src = activeSlide.src; 
            lightbox.classList.add('active'); 
        }
    }
}

// Tekli resimler için büyütme işlevi
function openSingleLightbox(buttonElement) {
    const container = buttonElement.closest('.image-container');
    if (container) {
        const img = container.querySelector('img');
        if (img) {
            const lightbox = document.getElementById('lightbox-overlay');
            const lightboxImg = document.getElementById('lightbox-img');
            
            if (lightbox && lightboxImg) {
                lightboxImg.src = img.src; // Resmi lightbox'a kopyala
                lightbox.classList.add('active'); // Lightbox'ı görünür yap
                lightbox.classList.add('single-image'); // Navigasyon oklarını gizlemek için sınıf ekle
            }
        }
    }
}

function closeLightbox(event) {
    // Sadece siyah arka plana tıklanırsa kapat (resmin kendisine tıklanırsa kapatma)
    if (event.target.id === 'lightbox-overlay') {
        const lightbox = document.getElementById('lightbox-overlay');
        lightbox.classList.remove('active');
        lightbox.classList.remove('single-image'); // Sınıfı temizle
    }
}


document.addEventListener('DOMContentLoaded', createEnhancedStarfield);


// =========================================
// LOCAL RAG ASİSTANI (CHATBOT WIDGET)
// =========================================
function initRagChatbot() {
    if (document.querySelector('.rag-chat-btn')) return;

    // Chatbot Açma/Kapama Butonu
    const chatBtn = document.createElement('button');
    chatBtn.className = 'rag-chat-btn';
    chatBtn.title = 'Local RAG Asistanı ile Sohbet Et';
    chatBtn.innerHTML = '<i class="fa-solid fa-robot"></i>';

    // Chatbot Penceresi
    const chatWindow = document.createElement('div');
    chatWindow.className = 'rag-chat-window';
    chatWindow.innerHTML = `
        <div class="rag-chat-header">
            <div class="rag-chat-header-title">
                <i class="fa-solid fa-robot"></i>
                <span>Local RAG Asistanı</span>
                <span class="rag-status-dot" title="Çevrimiçi"></span>
            </div>
            <button class="rag-chat-close" title="Kapat"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="rag-chat-messages">
            <div class="rag-message assistant">
                Merhaba! Ben Mehmet Burak Menteşe'nin kişisel yapay zeka asistanıyım. Projeler, blog yazıları veya sitede anlamadığın teknik terimler hakkında bana dilediğini sorabilirsin! 🤖
            </div>
        </div>
        <div class="rag-chat-input-area">
            <input type="text" class="rag-chat-input" placeholder="Bir soru sorun..." />
            <button class="rag-chat-send-btn" title="Gönder"><i class="fa-solid fa-paper-plane"></i></button>
        </div>
    `;

    document.body.appendChild(chatBtn);
    document.body.appendChild(chatWindow);

    const closeBtn = chatWindow.querySelector('.rag-chat-close');
    const input = chatWindow.querySelector('.rag-chat-input');
    const sendBtn = chatWindow.querySelector('.rag-chat-send-btn');
    const messagesContainer = chatWindow.querySelector('.rag-chat-messages');

    // Pencereyi Aç/Kapat
    function toggleChat() {
        const isOpen = chatWindow.classList.toggle('open');
        chatBtn.classList.toggle('active', isOpen);
        if (isOpen) {
            chatBtn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
            setTimeout(() => input.focus(), 150);
        } else {
            chatBtn.innerHTML = '<i class="fa-solid fa-robot"></i>';
        }
    }

    chatBtn.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    // Mesaj Gönderme
    async function sendMessage() {
        const messageText = input.value.trim();
        if (!messageText) return;

        // Kullanıcı mesajını ekle
        appendMessage('user', messageText);
        input.value = '';

        // Yazıyor... göstergesini ekle
        const typingIndicator = document.createElement('div');
        typingIndicator.className = 'rag-typing';
        typingIndicator.innerHTML = '<span></span><span></span><span></span>';
        messagesContainer.appendChild(typingIndicator);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        try {
            const response = await fetch('http://127.0.0.1:8000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: messageText })
            });

            typingIndicator.remove();

            if (response.ok) {
                const data = await response.json();
                appendMessage('assistant', data.response);
            } else {
                appendMessage('assistant', 'Üzgünüm, cevap üretilirken bir hata oluştu.');
            }
        } catch (error) {
            typingIndicator.remove();
            appendMessage('assistant', '⚠️ Yerel sunucuya bağlanılamadı. Lütfen "python main.py" API sunucusunun arka planda çalıştığından emin olun.');
        }
    }

    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `rag-message ${sender}`;
        msgDiv.textContent = text;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });
}

document.addEventListener('DOMContentLoaded', initRagChatbot);
