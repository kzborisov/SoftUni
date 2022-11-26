function extractText() {
  document.getElementById("result").value = [...document.querySelectorAll("li")]
    .map((el) => el.textContent)
    .join("\n");
}
