// Task 4 - Movie Tickets

function movieTickets(input){
    // Read Input
    let a1 = Number(input.shift());
    let a2 = Number(input.shift());
    let n = Number(input.shift());

    // Logic
    for (let i = a1; i <= a2 - 1; i++){
        if (i % 2 === 1){
            for (let j = 1; j <= n-1; j++){
                for (let k = 1; k <= (n / 2 - 1); k++){
                    if ((j + k + i) % 2 === 1){
                        console.log(`${String.fromCharCode(i)}-${j}${k}${i}`);
                    }
                }
            }
        }
    }
}

movieTickets(["86",
"88",
"4"])

