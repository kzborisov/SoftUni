function toggle() {
  const btn = document.querySelector(".head .button");
  const extra = document.getElementById("extra");

  if (btn.textContent === "More") {
    btn.textContent = "Less";
    extra.style.display = "block";
  } else {
    btn.textContent = "More";
    extra.style.display = "none";
  }
}
