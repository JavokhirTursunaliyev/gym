
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});


document.querySelectorAll('nav ul li a[href^="#"]').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});


const loginBtn = document.getElementById("login-btn");
const loginModal = document.getElementById("login-modal");
const closeModal = document.querySelector(".close");
const signupForm = document.getElementById("signup-form");


if (loginBtn && loginModal) {
    loginBtn.addEventListener("click", function () {
        loginModal.style.display = "flex";
    });
}


if (closeModal && loginModal) {
    closeModal.addEventListener("click", function () {
        loginModal.style.display = "none";
    });
}


window.addEventListener("click", function (event) {
    if (event.target === loginModal) {
        loginModal.style.display = "none";
    }
});

if (signupForm) {
    signupForm.addEventListener("submit", function (event) {
        event.preventDefault(); 
        alert("Registration Successful!");
        loginModal.style.display = "none";
    });
}
