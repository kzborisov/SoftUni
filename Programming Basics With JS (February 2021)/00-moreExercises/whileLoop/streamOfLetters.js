// Task 3 - Report System

function streamOfLetters(input) {
    // Read Input
    let str = input
        // Filter non alphabetic characters
      .filter(line => line.match(/^[a-z]$/i))
        // Join characters to a string
      .join("");

    // Logic
    const getIndexes = (text) => [text.search(/n/), text.search(/o/), text.search(/c/)];
    
    let message = '';
  
    let indexes;
    while (Math.min(...(indexes = getIndexes(str))) >= 0) {
        let chars = Math.max(...indexes) + 1;
        
        let word = str.substring(0, chars)
        .replace(/n/, "")
        .replace(/o/, "")
        .replace(/c/, "");
        message += word + ' ';
  
      str = str.substring(chars);
    }

    // Print Result
    console.log(message);
}

streamOfLetters([
    "%",
    "!",
    "c",
    "^",
    "B",
    "`",
    "o",
    "%",
    "o",
    "o",
    "M",
    ")",
    "{",
    "n",
    "\\",
    "A",
    "D",
    "End"
]);
