function christmasGifts(input) {
    // Read Input
    let age = input.shift();

    // Logic
    let adults = 0;
    let kids = 0;

    while (age != "Christmas"){
        let currentAge = Number(age);

        if (age <= 16) kids++;
        else adults++;

        age = input.shift();
    }

    let toysPrice = kids * 5;  // Each toy is 5 lv
    let sweaterPrice = adults * 15;  // Each sweater is 15 lv

    // Print result
    console.log(`Number of adults: ${adults}`);
    console.log(`Number of kids: ${kids}`);
    console.log(`Money for toys: ${toysPrice}`);
    console.log(`Money for sweaters: ${sweaterPrice}`);
}

christmasGifts(["16",
"20",
"46",
"12",
"8",
"20",
"49",
"Christmas"]);