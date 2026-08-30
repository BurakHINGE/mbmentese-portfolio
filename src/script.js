// Toggle Language function
function toggleLanguage(event) {
    event.preventDefault();
    currentLang = currentLang === 'tr' ? 'en' : 'tr';
    document.documentElement.lang = currentLang;
    
    // Translate all elements with data-translate attribute
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        if (translations[currentLang][key]) {
            if (key === 'modalText' || key === 'contactHeroText') {
                element.innerHTML = translations[currentLang][key];
            } else {
                element.textContent = translations[currentLang][key];
            }
        }
    });

    // Update Active Language Indicators
    if (currentLang === 'tr') {
        document.getElementById('lang-tr').classList.add('lang-active');
        document.getElementById('lang-en').classList.remove('lang-active');
    } else {
        document.getElementById('lang-tr').classList.remove('lang-active');
        document.getElementById('lang-en').classList.add('lang-active');
    }
}

// Typewriter Effect for the Domain Highlight
function initTypewriter() {
    const text = "marmaracyber.com";
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

    function animate() {
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

document.addEventListener('DOMContentLoaded', createEnhancedStarfield);
