function validate() {
    const emailField = document.getElementById("email");

    emailField.addEventListener("change", onChange);

    function onChange(e) {
        const pattern = /^[a-z]+@[a-z]+\.[a-z]+$/;

        if (pattern.test(e.target.value)) {
            e.target.classList.remove("error");
        } else {
            e.target.classList.add("error");
        }
    }
}
