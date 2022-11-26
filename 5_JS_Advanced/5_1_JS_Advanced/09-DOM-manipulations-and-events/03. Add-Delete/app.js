function addItem() {
    const ul = document.getElementById("items");
    const newValue = document.getElementById("newItemText");

    if (newValue.value === "") {
        alert("Please enter something!");
    }
    const liElement = document.createElement("li");
    liElement.textContent = newValue.value;

    const deleteBtn = document.createElement("a");
    deleteBtn.href = "#";
    deleteBtn.textContent = "[Delete]";
    liElement.appendChild(deleteBtn);

    deleteBtn.addEventListener("click", (e) => {
        e.target.parentElement.remove();
    });

    ul.appendChild(liElement);
    newValue.value = "";
}
