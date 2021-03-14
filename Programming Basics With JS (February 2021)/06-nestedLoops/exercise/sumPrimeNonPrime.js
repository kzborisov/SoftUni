// Task 3 - Sum Prime Non Prime

function sumPrime(input) {
    // Read Input
    let num = input.shift();

    // Logic
    let primeSum = 0;
    let nonPrimeSum = 0;

    while (num != "stop"){
        let current = Number(num);
        num = input.shift();
        if (current < 0){
            console.log("Number is negative.");
            continue;
        }

        let isPrime = true;

        for (let i = 2; i <= Math.sqrt(current); i++){
            if (current % i == 0){
                isPrime = false;
                break;
            }
        }

        if (isPrime) primeSum += current;
        else nonPrimeSum += current;
    }
    console.log(`Sum of all prime numbers is: ${primeSum}`);
    console.log(`Sum of all non prime numbers is: ${nonPrimeSum}`);
}

sumPrime(["3",
"9",
"0",
"7",
"19",
"4",
"stop"]);