function sumTable() {
    const data = Array.from(document.querySelectorAll('tr')).slice(1, -1);
    let sum = 0;

    for (let i = 0; i < data.length; i++) {
        console.log(data[i].lastChild);
        sum += Number(data[i].lastChild.textContent);
    }

    document.getElementById('sum').textContent = sum;
}
