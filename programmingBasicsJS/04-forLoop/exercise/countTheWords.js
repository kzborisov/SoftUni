// Task 5 - Count The Words

function countTheWords(input) {
    // Read Input
    let text = input[0];

    // Logic
    let words = text.split(" ").length;

    // Print result
    if (words > 10) {
        console.log(`The message is too long to be send! Has ${words} words.`);
    } else {
        console.log("The message was send successfully!");
    }
}

countTheWords(["Hello there"]);