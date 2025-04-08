// Mobile Navigation Toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Team card hover effect
document.querySelectorAll('.member-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-10px) scale(1.02)';
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) scale(1)';
    });
});

// Responsive adjustments
function adjustLayout() {
    const screenWidth = window.innerWidth;
    const teamCards = document.querySelectorAll('.member-card');

    if (screenWidth < 768) {
        teamCards.forEach(card => {
            card.style.margin = '1rem 0';
        });
    }
}

window.addEventListener('resize', adjustLayout);
adjustLayout();