document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- 2. Mobile Navigation Toggle ---
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    const navLinksItems = document.querySelectorAll('.nav-links li');

    hamburger.addEventListener('click', () => {
        // Toggle Nav Menu
        navLinks.classList.toggle('nav-active');
        
        // Hamburger Animation
        hamburger.classList.toggle('toggle');

        // Animate Links Entrance
        navLinksItems.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                // Memberikan delay bertingkat agar muncul satu per satu
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
    });

    // Menutup menu saat link diklik (UX yang baik untuk one-page scroll)
    navLinksItems.forEach(item => {
        item.addEventListener('click', () => {
            if (navLinks.classList.contains('nav-active')) {
                navLinks.classList.remove('nav-active');
                hamburger.classList.remove('toggle');
                navLinksItems.forEach((link) => {
                    link.style.animation = '';
                });
            }
        });
    });
});