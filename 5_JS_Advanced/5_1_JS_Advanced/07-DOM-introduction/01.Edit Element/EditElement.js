function editElement(elem, match, replacer) {
  const pattern = new RegExp(match, "g");
  const text = elem.textContent;
  const result = text.replace(pattern, replacer);
  elem.textContent = result;
}
