function solve() {
  const text = document.getElementById("text").value;
  const namingConvention = document.getElementById("naming-convention").value;
  const result = document.getElementById("result");

  function toCamelCase(sentenceCase) {
    var out = "";
    sentenceCase.split(" ").forEach(function (el, idx) {
      var add = el.toLowerCase();
      out += idx === 0 ? add : add[0].toUpperCase() + add.slice(1);
    });
    return out;
  }

  if (namingConvention === "Camel Case") {
    result.textContent = toCamelCase(text);
  } else if (namingConvention === "Pascal Case") {
    result.textContent = text
      .replace(/\w+/g, function (w) {
        return w[0].toUpperCase() + w.slice(1).toLowerCase();
      })
      .replace(/\s/g, "");
  } else {
    result.textContent = "Error!";
  }
}
