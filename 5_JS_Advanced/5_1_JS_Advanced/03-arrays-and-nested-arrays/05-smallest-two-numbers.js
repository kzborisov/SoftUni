function smallestTwoNumbers(inputArr) {
    return inputArr
        .sort((a, b) => a - b)
        .slice(0, 2)
        .join(' ');
}

console.log(smallestTwoNumbers([3, 0, 10, 4, 7, 3]));
