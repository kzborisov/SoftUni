function extractIncreasingSubsequenceFromArray(input) {
    let result = [];
    let biggest = input[0];

    for (let i = 0; i < input.length; i++) {
        let currentNum = input[i];

        if (currentNum >= biggest) {
            result.push(currentNum);
            biggest = currentNum;
        }
    }

    return result;
}

console.log(extractIncreasingSubsequenceFromArray());
