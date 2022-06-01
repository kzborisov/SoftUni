function biggestElement(matrix) {
    let rowsBiggestNumber = [];
    for (const row of matrix) {
        rowsBiggestNumber.push(Math.max(...row));
    }
    return Math.max(...rowsBiggestNumber);
}

console.log(
    biggestElement([
        [3, 5, 7, 12],
        [-1, 4, 33, 2],
        [8, 3, 0, 4],
    ])
);
