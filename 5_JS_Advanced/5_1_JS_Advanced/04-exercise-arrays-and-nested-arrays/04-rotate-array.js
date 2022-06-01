function rotateArray(input, num) {
    let result = input.slice();

    for (let i = 0; i < num; i++) {
        result.unshift(result.pop());
    }
    return result.join(' ');
}

console.log(rotateArray(['Banana', 'Orange', 'Coconut', 'Apple'], 15));
