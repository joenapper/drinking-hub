const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');

// Toggle Nav
function navSlide() {
    burger.addEventListener('click', () => {
        // Overlay Slide In
        nav.classList.toggle('nav-active');
        // Links Slide In
        linkSlide();
        // Burger Animation
        burger.classList.toggle('burger-toggle');
    });
};

// Links Slide In
function linkSlide() {
    navLinks.forEach((link, index) => {
        if(link.style.animation) {
            link.style.animation = ''
        } else {
            link.style.animation = `navLinkFade 1.0s ease forwards ${index / 5 + 0.4}s`;
        };
    });
}; 

navSlide()

const modal = document.getElementById('modalPopup');
const popUp = document.getElementById('delValidation');
const closeModalBtn = document.getElementsByClassName('closeModalBtn')[0];

popUp.addEventListener('click', openModal);
closeModalBtn.addEventListener('click', closeModal);

function openModal() {
    modal.style.display = 'block';
}

function closeModal() {
    modal.style.display = 'none'
}