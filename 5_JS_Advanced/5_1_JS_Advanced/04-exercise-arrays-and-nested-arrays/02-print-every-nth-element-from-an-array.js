function printEveryNthElement(input, num) {
    return input.filter((_, i) => i % num === 0);
}

console.log(printEveryNthElement(['dsa', 'asd', 'test', 'tset'], 2));
