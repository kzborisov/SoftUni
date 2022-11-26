function deleteByEmail() {
    const tableRows = [...document.querySelectorAll("tbody tr")];
    const input = document.querySelector('input[name="email"]');

    let isFound = false;

    tableRows.filter((row) => {
        if (row.children[1].textContent == input.value) {
            row.remove();
            isFound = true;
        }
    });

    document.getElementById("result").textContent = isFound
        ? "Deleted."
        : "Not found.";
}
