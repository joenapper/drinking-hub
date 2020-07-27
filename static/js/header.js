const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');

// Toggle Nav
function navSlide() {
    burger.addEventListener('click', () => {
        // Overlay Slide In
        nav.classList.toggle('nav-active');
    });
};

navSlide()