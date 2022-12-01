function lockedProfile() {
    [...document.querySelectorAll(".profile button")].forEach((p) =>
        p.addEventListener("click", onClick)
    );

    function onClick(e) {
        const profile = e.target.parentElement;
        const isUnlocked = profile.querySelector(
            'input[type="radio"][value="unlock"]'
        ).checked;

        if (isUnlocked) {
            const hiddenFields = profile.querySelector("div");
            if (e.target.textContent == "Show more") {
                hiddenFields.style.display = "block";
                e.target.textContent = "Hide it";
            } else {
                e.target.textContent = "Show more";
                hiddenFields.style.display = "none";
            }
        }
    }
}
