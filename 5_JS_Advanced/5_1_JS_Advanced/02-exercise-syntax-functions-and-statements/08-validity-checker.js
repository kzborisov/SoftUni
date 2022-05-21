function validityChecker(x1, y1, x2, y2) {
    function isValid(x1, y1, x2, y2) {
        let distance = Math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2);
        let isValidResult = Number.isInteger(distance) ? 'valid' : 'invalid';

        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${isValidResult}`);
    }

    isValid(x1, y1, 0, 0);
    isValid(x2, y2, 0, 0);
    isValid(x1, y1, x2, y2);
}

validityChecker(3, 0, 0, 4);
