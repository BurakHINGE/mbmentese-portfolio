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