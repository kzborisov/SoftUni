function colorize() {
  [...document.querySelectorAll("tr:nth-child(2n)")].forEach(
    (e) => (e.style.background = "teal")
  );
}
