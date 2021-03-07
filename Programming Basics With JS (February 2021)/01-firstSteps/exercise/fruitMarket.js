// Task 7 - Fruit Market
function calcTotalSum(input) {
    let strawberryPrice = Number(input[0]);
    let bananasKg = Number(input[1]);
    let orangesKg = Number(input[2]);
    let raspberryKg = Number(input[3]);
    let strawberryKg = Number(input[4]);

    let raspberryPriceKg = strawberryPrice / 2;
    let priceRaspberry = raspberryKg * raspberryPriceKg;

    let orangesPriceKg = raspberryPriceKg - (0.4 * raspberryPriceKg);
    let priceOranges = orangesKg * orangesPriceKg;

    let bananasPriceKg = raspberryPriceKg - (0.8 * raspberryPriceKg);
    let priceBananas = bananasKg * bananasPriceKg;

    let priceStrawberry = strawberryPrice * strawberryKg;
    let result = priceRaspberry + priceOranges + priceBananas + priceStrawberry;
    console.log(result);
}

calcTotalSum(["63.5", "3.57", "6.35", "8.15", "2.5"])