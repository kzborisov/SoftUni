function diagonalSums(matrix) {
    let primary = 0;
    let secondary = 0;
    for (let row = 0; row < matrix.length; row++) {
        primary += matrix[row][row];
        secondary += matrix[row][matrix.length - row - 1];
    }

    return `${primary} ${secondary}`;
}

console.log(
    diagonalSums([
        [20, 40],
        [10, 60],
    ])
);
