function lastKNumbersSequence(n, k) {
    let result = [1];
    while (result.length < n) {
        let lastKElements = result.slice(-k);
        let lastKElementsSum = lastKElements.reduce((acc, num) => {
            return acc + num || 0;
        }, 0);
        result.push(lastKElementsSum);
    }
    return result;
}

console.log(lastKNumbersSequence(8, 2));
