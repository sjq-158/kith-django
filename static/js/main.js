document.addEventListener("DOMContentLoaded", function () {
    // Password visibility toggle logic
    const toggleButtons = document.querySelectorAll(".toggle-password");

    toggleButtons.forEach(button => {
        button.addEventListener("click", function () {
            const targetId = this.getAttribute("data-target");
            const passwordInput = document.getElementById(targetId);

            if (passwordInput) {
                if (passwordInput.type === "password") {
                    passwordInput.type = "text";
                    this.textContent = "Hide";
                } else {
                    passwordInput.type = "password";
                    this.textContent = "Show";
                }
            }
        });
    });
});