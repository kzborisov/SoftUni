function solve() {
    const [input, output] = [...document.querySelectorAll("textarea")];
    const [generatBtn, buyBtn] = [...document.querySelectorAll("button")];
    const tableBody = document.querySelector(".table tbody");

    generatBtn.addEventListener("click", generate);
    buyBtn.addEventListener("click", buy);

    let items = [];

    function generate() {
        const data = JSON.parse(input.value);

        data.forEach((item) => {
            const tr = document.createElement("tr");

            createColumn("img", item.img);
            createColumn("p", item.name);
            createColumn("p", item.price);
            createColumn("p", item.decFactor);
            createColumn("td");

            function createColumn(type, content) {
                const col = document.createElement("td");
                if (type == "img") {
                    const img = document.createElement("img");
                    img.src = content;
                    col.appendChild(img);
                } else if (type == "p") {
                    const p = document.createElement("p");
                    p.textContent = content;
                    col.appendChild(p);
                } else {
                    const checkbox = document.createElement("input");
                    checkbox.type = "checkbox";
                    col.appendChild(checkbox);
                }

                tr.appendChild(col);
            }

            tableBody.appendChild(tr);
            items.push(tr);
        });
    }

    function buy() {
        const rows = items.filter(
            (item) => item.children[4].children[0].checked
        );

        let totalPrice = 0;
        let averageDecFactor = 0;
        const names = [];

        rows.forEach((item) => {
            const rowChildren = item.children;
            const name = rowChildren[1].children[0].textContent;
            const price = rowChildren[2].children[0].textContent;
            const decFactor = rowChildren[3].children[0].textContent;

            totalPrice += Number(price);
            averageDecFactor += Number(decFactor);
            names.push(name);
        });

        averageDecFactor /= rows.length;

        const result = [
            `Bought furniture: ${names.join(", ")}`,
            `Total price: ${totalPrice.toFixed(2)}`,
            `Average decoration factor: ${averageDecFactor}`,
        ];
        output.textContent = result.join("\n");
    }
}
