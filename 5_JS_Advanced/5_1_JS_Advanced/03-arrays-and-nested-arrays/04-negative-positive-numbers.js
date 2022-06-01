function negativePositiveNumbers(inputArr) {
    let result = [];
    for (let num of inputArr) {
        if (num < 0) {
            result.unshift(num);
        } else {
            result.push(num);
        }
    }
    result.forEach((num) => console.log(num));
}

negativePositiveNumbers([0, -1, -2, 4, 1]);
