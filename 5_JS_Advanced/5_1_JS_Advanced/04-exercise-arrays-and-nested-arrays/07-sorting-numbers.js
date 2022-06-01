function sortingNumbers(input) {
    let sortedInput = input.sort((a, b) => a - b);
    let result = [];

    while (sortedInput.length) {
        result.push(sortedInput.shift());
        result.push(sortedInput.pop());
    }
    return result;
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));
