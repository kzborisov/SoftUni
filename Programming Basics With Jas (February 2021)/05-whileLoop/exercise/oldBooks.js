// Task 1 - Old Books

function oldBooks(input) {
    // Read Input
    let searchedBook = input.shift();

    // Logic
    let counter = 0;

    while (true) {
        let nextBook = input.shift();
        counter++;
        if (nextBook === searchedBook){
            console.log(`You checked ${counter-1} books and found it.`);
            break;
        }

        if (nextBook === "No More Books"){
            console.log(`The book you search is not here!`);
            console.log(`You checked ${counter-1} books.`);
            break;
        }
    }
}

oldBooks(["Bourne",
"True Story",
"Forever",
"More Space",
"The Girl",
"Spaceship",
"Strongest",
"Profit",
"Tripple",
"Stella",
"The Matrix",
"Bourne"]);