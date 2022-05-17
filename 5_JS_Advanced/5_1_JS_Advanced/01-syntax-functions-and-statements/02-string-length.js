function stringLenght(first, second, third) {
    let result = first.length + second.length + third.length;
    let averageLength = Math.floor(result / 3);
    console.log(result);
    console.log(averageLength);
}

stringLenght("chocolate", "ice cream", "cake");
