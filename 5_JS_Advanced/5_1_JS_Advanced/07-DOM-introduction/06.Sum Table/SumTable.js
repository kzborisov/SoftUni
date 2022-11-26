function sumTable() {
  const prices = [...document.querySelectorAll("tr td:last-child")].map((el) =>
    Number(el.textContent)
  );

  const result = prices.reduce((acc, red) => acc + red, 0);

  document.getElementById("sum").textContent = result;
}
