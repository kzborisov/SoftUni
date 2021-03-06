// Task 10 - Diamond

function drawFig(input) {
    let n = Number(input.shift());

    let stars = 1;
    let dashes = (n - stars) / 2;
    let midDashes = -1;
    if (n % 2 == 0) {
        stars = 2;
        midDashes = 0;
    }

    // Upper half
    for (let row = 0; row <= (n - 1) / 2; row++) {
        if (midDashes >= 0){
            console.log(
                "-".repeat(dashes) +
                "*" +
                "-".repeat(midDashes)+
                "*" +
                "-".repeat(dashes)
                );
        } else {
            console.log(
                "-".repeat(dashes) +
                "*" +
                "-".repeat(dashes)
                );
        }
        dashes--;
        midDashes+=2;
    }

    dashes = 1;
    midDashes = n - 4;

    // Bottom half
    for (let row = 1; row < (n /2); row++){
        if (midDashes >= 0){
            console.log(
                "-".repeat(dashes) +
                "*" +
                "-".repeat(midDashes)+
                "*" +
                "-".repeat(dashes)
                );
        } else {
            console.log(
                "-".repeat(dashes) +
                "*" +
                "-".repeat(dashes)
                );
        }
        dashes++;
        midDashes-=2;
    }
}

drawFig(["2"]);