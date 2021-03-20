function beerAndChips(input) {
    // Read Input
    let name = input.shift();
    let budget = Number(input.shift());
    let beersCount = Number(input.shift());
    let chipsCount = Number(input.shift());

    // Logic
    let beerPrice = beersCount * 1.20;
    let chipsPrice = Math.ceil(chipsCount * (beerPrice * 0.45));
    let totalPrice = beerPrice + chipsPrice;

    // Print result
    if (totalPrice <= budget){
        let moneyLeft = (budget - totalPrice).toFixed(2);
        console.log(`${name} bought a snack and has ${moneyLeft} leva left.`)
    } else {
        let moreMoney = (totalPrice - budget).toFixed(2)
        console.log(`${name} needs ${moreMoney} more leva!`)
    }
}

beerAndChips(["Valentin", "5", "2", "4"]);