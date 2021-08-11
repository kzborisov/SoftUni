// Task 3 - Logistics

function logistics(input) {
    // Read Input
    let cargoCount = Number(input[0]);

    // Logic
    let price = 0;
    let totalWeight = 0;
    let wheelsType = {
        'bus': 0,
        'truck': 0,
        'train': 0
    };

    for (let i=1; i<=cargoCount; i++){
        let weight = Number(input[i]);

        totalWeight += weight;

        if (weight >= 12){
            price += weight * 120;
            wheelsType['train'] += weight;
        } else if (weight >= 4){
            price += weight *175;
            wheelsType['truck'] += weight;
        } else {
            price += weight * 200;
            wheelsType['bus'] += weight;
        }

    }
    let average = price / totalWeight;

    // Print Result
    console.log(average.toFixed(2));
    for (key in wheelsType){
        console.log(`${(wheelsType[key]/totalWeight*100).toFixed(2)}%`);
    }
}

logistics(["4", "1", "5", "16", "3"]);