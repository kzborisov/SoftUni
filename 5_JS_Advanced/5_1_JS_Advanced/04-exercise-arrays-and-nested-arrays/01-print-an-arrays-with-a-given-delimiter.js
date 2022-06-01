function printAnArrayWithAGivenDelimiter(input, delimiter) {
    return input.join(delimiter);
}

console.log(
    printAnArrayWithAGivenDelimiter(
        ['One', 'Two', 'Three', 'Four', 'Five'],
        '-'
    )
);
