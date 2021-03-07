// Task 6 - Vowels Sum

function vowelSum(input) {
    // Read Input
    let str = input[0];

    // Logic
    let vowesMap = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    };
    let sum = 0;

    for (var i = 0; i < str.length; i++) {
        if (str[i] in vowesMap){
            sum += vowesMap[str[i]];
        }
    }

    // Print
    console.log(sum);
}

vowelSum(['bamboo'])