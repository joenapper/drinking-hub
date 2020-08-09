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


// Delete Validation Pop up
const modal = document.getElementById('modalPopup');
const popUp = document.getElementById('delValidation');
const closeModalBtn = document.getElementsByClassName('closeModalBtn')[0];
const noValidation = document.getElementById('noVal');

popUp.addEventListener('click', openModal);
closeModalBtn.addEventListener('click', closeModal);
noValidation.addEventListener('click', closeModal);
window.addEventListener('click', clickOutside);

// When the delete button is clicked the pop up will appear
function openModal() {
    modal.style.display = 'block';
}
// When either the 'No' or 'X' buttons are clicked, the pop up will close 
function closeModal() {
    modal.style.display = 'none'
}
// If the user clicks anywhere but the popup, it will automatically close
function clickOutside(e) {
    if(e.target == modal) {
        modal.style.display = 'none'
    }
}