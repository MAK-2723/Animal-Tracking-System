// Mobile Navigation Toggle
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when clicking a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Demo button interaction
const demoBtn = document.getElementById('demoBtn');
demoBtn.addEventListener('click', () => {
    // For demo purposes - would link to actual demo page
    alert('Redirecting to live demo...');
    // window.location.href = 'demo.html';
});

// Dynamic feature card animation
const featureCards = document.querySelectorAll('.feature-card');
featureCards.forEach((card, index) => {
    card.style.transitionDelay = ${index * 0.1}s;
});

// Check for user session
document.addEventListener('DOMContentLoaded', () => {
    const currentUser = localStorage.getItem('currentUser');
    if(currentUser) {
        // User is logged in - could update UI
        console.log('User session active:', JSON.parse(currentUser));
    }
});

// Responsive adjustments
function adjustLayout() {
    const screenWidth = window.innerWidth;
    const heroTitle = document.querySelector('.hero h1');
    
    if(screenWidth < 500) {
        heroTitle.style.fontSize = '2rem';
    } else {
        heroTitle.style.fontSize = '3.5rem';
    }
}

window.addEventListener('resize', adjustLayout);
adjustLayout(); // Initialize
