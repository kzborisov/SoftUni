function roomPainting(input) {
    // Read Input
    let cansCount = Number(input.shift());
    let wallpapersCount = Number(input.shift());
    let glovesPrice = Number(input.shift());
    let brushPrice = Number(input.shift());

    // Logic
    let paintPrice = cansCount * 21.50;
    let wallpapersPrice = wallpapersCount * 5.20;
    let glovesNeeded = Math.ceil(wallpapersCount * 0.35);
    let brushNeeded = Math.floor(cansCount * 0.48);
    let totalGlovesCount = glovesNeeded * glovesPrice;
    let totalBrushPrice = brushNeeded * brushPrice;
    let totalPrice = paintPrice + wallpapersPrice + totalGlovesCount + totalBrushPrice    
    let deliveryCost = totalPrice/15;

    // Print result
    console.log(`This delivery will cost ${deliveryCost.toFixed(2)} lv.`);
}

roomPainting(["21", "18", "5", "2.2"]);