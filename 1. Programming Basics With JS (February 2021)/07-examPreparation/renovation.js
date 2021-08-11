// Task 5 - Renovations

function renovations(input){
    // Read Input
    let height = Number(input.shift());
    let width = Number(input.shift());
    let totalAreaPercent = Number(input.shift());

    // Logic
    let totalArea = height * width * 4;
    let paintingArea = Math.ceil(totalArea - (totalArea * (totalAreaPercent/100)));


    let paint = input.shift();

    while (paint !== "Tired!"){
        let currentPaint = Number(paint);

        paintingArea -= currentPaint;

        if (paintingArea <= 0){
            break;
        }

        paint = input.shift();
    }

    if (Number(paintingArea) == 0){
        console.log(`All walls are painted! Great job, Pesho!`);
    } else if (paint === "Tired!"){
        console.log(`${paintingArea} quadratic m left.`);
    } else {
        console.log(`All walls are painted and you have ${Math.abs(paintingArea)} l paint left!`);
    }
}

renovations(["2",
"3",
"25",
"6",
"7",
"8"])

