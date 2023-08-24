document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");

    registerForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        // Implement registration logic here
    });

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const loginUsername = document.getElementById("login-username").value;
        const loginPassword = document.getElementById("login-password").value;
        // Implement login logic here
    });
});
