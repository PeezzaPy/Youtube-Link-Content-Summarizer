const navToggle = document.querySelector('#navToggle');
const nav = document.querySelector('.nav-links');
const buttons = document.querySelector('.buttons');

navToggle.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    buttons.classList.toggle('buttons-open');
});