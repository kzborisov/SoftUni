function biggerHalf(inputArr) {
    inputArr.sort((a, b) => b - a);
    let middle = Math.round(inputArr.length / 2);
    return inputArr.slice(0, middle).sort((a, b) => a - b);
}

console.log(biggerHalf([4, 7, 2, 5]));
console.log(biggerHalf([3, 19, 14, 7, 2, 19, 6]));
