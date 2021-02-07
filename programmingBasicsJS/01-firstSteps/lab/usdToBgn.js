// Task 1 - USD to BGN converter
function usdToBgn(input) {
    let usd = Number(input[0]);
    let bgnMultiplier = 1.79549;
    let result = usd * bgnMultiplier;
    console.log(result);
}

usdToBgn(["12.5"]);