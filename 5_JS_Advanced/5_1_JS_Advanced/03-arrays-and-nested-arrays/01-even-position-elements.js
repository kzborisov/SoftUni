function evenPositionElements(input) {
    let result = [];

    for (let i = 0; i < input.length; i += 2) {
        result.push(input[i]);
    }

    console.log(result.join(' '));
}

evenPositionElements(['20', '40', '60']);
