function processOddPositions(inputArr) {
    return inputArr
        .filter((_, index) => index % 2 === 1)
        .map((num) => num * 2)
        .reverse()
        .join(' ');
}

console.log(processOddPositions([10, 15, 20, 25]));
console.log(processOddPositions([3, 0, 10, 4, 7, 3]));
