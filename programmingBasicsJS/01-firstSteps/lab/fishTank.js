// Task 8 - Fish Tank
function calcLiters(input) {
    let aqLength = Number(input[0]);
    let aqWidth = Number(input[1]);
    let aqHeight = Number(input[2]);
    let percent = Number(input[3]);

    let totalLiters = (aqLength * aqWidth * aqHeight) * 0.001;
    let result = totalLiters * (1 - (percent * 0.01));
    console.log(result);
}

calcLiters(["105", "77", "89", "18.5"]);