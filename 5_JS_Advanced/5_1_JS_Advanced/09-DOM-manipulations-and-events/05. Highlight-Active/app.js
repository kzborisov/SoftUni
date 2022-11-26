function focused() {
    const inputFields = [...document.querySelectorAll("input")];

    inputFields.forEach((i) => {
        i.addEventListener("focus", (e) => {
            e.target.parentElement.classList.add("focused");
        });

        i.addEventListener("blur", (e) => {
            e.target.parentElement.classList.remove("focused");
        });
    });
}
