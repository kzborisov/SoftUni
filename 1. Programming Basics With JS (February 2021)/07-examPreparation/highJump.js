// Task 6 - High Jump

function highJump(input){
    // Read Input
    let desiredHeight = Number(input.shift());

    // Logic
    let isSuccessfull = false;
    let height = desiredHeight - 30;
    let jumps = 0;
    let tries = 0;

    while(true){
        let currentHeight = Number(input.shift());
        jumps++;

        if (currentHeight > height){
            // If the current height reached is more than the height set
            // add 5cm to the height;
            isSuccessfull = true;
            tries = 0;
            height += 5;
        } else {
            tries++;
        }

        if ((height > desiredHeight) && isSuccessfull){
            // If the height is reached, return success
            console.log(`Tihomir succeeded, he jumped over ${desiredHeight}cm after ${jumps} jumps.`);
            break;
        }

        if ((tries % 3 === 0) && (!isSuccessfull)){
            // If after 3 tries the height is not reached, return fail.
            console.log(`Tihomir failed at ${height}cm after ${jumps} jumps.`);
            break;
        }
        isSuccessfull = false;
    }
}

highJump(["231",
"205",
"212",
"213",
"228",
"229",
"230",
"235"])
;

