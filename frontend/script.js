//user login and register

const logregBox = document.querySelector('.logreg-box');
const loginLink = document.querySelector('.login-link');
const registerlink = document.querySelector('.register-link');
var reveal = false;

registerlink.addEventListener('click', () => {
    logregBox.classList.add('active');
});

loginLink.addEventListener('click', () => {
    logregBox.classList.remove('active');
});

function reveal_password() {
    !reveal ? document.getElementById('password').type = 'text' : document.getElementById('password').type = 'password';
    reveal = !reveal;


    // document.getElementById('locked').display = 'none';


}

//
