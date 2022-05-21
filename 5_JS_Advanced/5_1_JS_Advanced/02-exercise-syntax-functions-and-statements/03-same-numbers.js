function sumOfDigits(number) {
    let sum = 0;

    while (number) {
        sum += number % 10;
        number = Math.floor(number / 10);
    }

    return sum;
}

function sameNumbers(number) {
    let numAsStr = String(number);
    let isSame = true;

    for (let i = 0; i < numAsStr.length - 1; i++) {
        if (numAsStr[i] !== numAsStr[i + 1]) {
            isSame = false;
            break;
        }
    }

    let sum = 0;
    let num = number;

    while (num) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }

    console.log(isSame);
    console.log(sum);
}

sameNumbers(2222222);
