function create(words) {
    const content = document.getElementById("content");
    words.forEach((word) => showWord(word));

    [...content.querySelectorAll("div")].forEach((div) =>
        div.addEventListener("click", (e) => {
            e.currentTarget.querySelector("p").style.display = "block";
        })
    );

    function showWord(word) {
        const div = document.createElement("div");
        content.appendChild(div);

        const p = document.createElement("p");
        p.style.display = "none";
        p.textContent = word;

        div.appendChild(p);
    }
}
