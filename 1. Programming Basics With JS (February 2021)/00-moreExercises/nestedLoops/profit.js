// Task 10 - Profit

function profit(input) {
    // Read Input
    let ones = Number(input.shift());
    let twos = Number(input.shift());
    let fives = Number(input.shift());
    let sum = Number(input.shift());

    // Logic
    for(let i = 0; i <= ones; i++) {
        for(let j = 0; j <= twos; j++) {
            for (let k = 0; k <= fives; k++) {
                if ((i * 1 + j * 2 + k * 5) === sum){
                    console.log(`${i} * 1 lv. + ${j} * 2 lv. + ${k} * 5 lv. = ${sum} lv.`);
                }
            }
        }
    }
}

profit(["5", "3", "1", "7"]);