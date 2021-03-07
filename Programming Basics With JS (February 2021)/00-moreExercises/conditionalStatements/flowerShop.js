// Task 7 - Flower Shop

function flowerShop(input) {
    // Read Input Data
    let magnolias = Number(input[0]);
    let zumbuls = Number(input[1]);
    let roses = Number(input[2]);
    let cactuses = Number(input[3]);
    let giftPrice = Number(input[4]);

    // Calculations
    let dictMap = {
        'magnolias': 3.25,
        'zumbuls': 4,
        'roses': 3.50,
        'cactuses': 8,
    };
    let totalSum = (
        magnolias * dictMap['magnolias'] +
        zumbuls * dictMap['zumbuls'] +
        roses * dictMap['roses'] +
        cactuses * dictMap['cactuses']
        ) * 0.95;  // 5% of the sum is paid for taxes
        let money = totalSum - giftPrice;

    // Print result
    if (money >= 0){
        console.log(`She is left with ${Math.floor(money)} leva.`)
    } else {
        console.log(`She will have to borrow ${Math.ceil(Math.abs(money))} leva.`)
    }
}

flowerShop(["15", "7", "5", "10", "100"]);