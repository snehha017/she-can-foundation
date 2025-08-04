const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');


registerBtn.addEventListener('click', () => {
    container.classList.add('active');
    document.body.classList.add('signup-active');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
    document.body.classList.remove('signup-active');
}); 