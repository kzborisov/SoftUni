function search() {
  const towns = [...document.querySelectorAll("li")];
  const searchText = document.getElementById("searchText").value.toLowerCase();
  const result = document.getElementById("result");

  let matches = 0;

  towns.forEach((town) => {
    const townText = town.textContent.toLowerCase();
    if (townText.includes(searchText)) {
      town.style.fontWeight = "bold";
      town.style.textDecoration = "underline";

      matches += 1;
    } else {
      town.style.fontWeight = "";
      town.style.textDecoration = "";
    }
  });

  //   for (const town of towns) {
  //   }

  result.textContent = `${matches} matches found`;
}
