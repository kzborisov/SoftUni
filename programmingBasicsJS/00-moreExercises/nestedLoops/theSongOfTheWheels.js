// Task 12 - The Song Of The Wheels

function theSongOfTheWheels(input) {
    // Read Input
    let n = Number(input.shift());

    // Logic
    let counter = 0;
    let password = "";

    for (let first = 1; first < 10; first++){
        for (let second = 1; second < 10; second++){
            if (first < second){
                for (let third = 1; third < 10; third++){
                    for (let fourth = 1; fourth < 10; fourth++){
                        let isEqual = first * second + third * fourth === n;
                        if (third > fourth && isEqual){
                            process.stdout.write(`${first}${second}${third}${fourth} `);
                            counter++;
                            if (counter == 4){
                                password = `${first}${second}${third}${fourth}`;
                            }
                        }
                    }
                }
            }
        }
    }
    console.log();
    if (password.length > 0){
        console.log(`Password: ${password}`);
    } else {
        console.log(`No!`);
    }
}

theSongOfTheWheels(["11"]);