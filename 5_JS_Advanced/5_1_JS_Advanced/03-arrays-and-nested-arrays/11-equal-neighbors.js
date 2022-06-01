function equalNeighboors(matrix) {
    let pairsCount = 0;

    for (let row = 0; row < matrix.length - 1; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === matrix[row + 1][col]) {
                pairsCount++;
            }
            if (matrix[row][col] === matrix[row][col + 1]) {
                pairsCount++;
            }
            if (
                row === matrix.length - 2 &&
                matrix[row + 1][col] === matrix[row + 1][col + 1]
            ) {
                pairsCount++;
            }
        }
    }

    return pairsCount;
}

let matrix = [
    [2, 2, 5, 7, 4],
    [4, 0, 5, 3, 4],
    [2, 5, 5, 4, 2],
];

console.log(equalNeighboors(matrix));
