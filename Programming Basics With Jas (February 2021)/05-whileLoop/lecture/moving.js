// Task 9 - Moving *

function moving(input) {
    // Read Input
    let width = Number(input.shift());
    let length = Number(input.shift());
    let height = Number(input.shift());

    // Logic
    let freeSpace = width * length * height;
    let occupiedSpace = 0;
    let command = input.shift();

    while (command != "Done"){
        let currentCubic = Number(command);

        occupiedSpace += currentCubic;

        if (freeSpace < occupiedSpace){
            let spaceLeft = occupiedSpace - freeSpace;
            console.log(`No more free space! You need ${spaceLeft} Cubic meters more.`);
            break;
        }
        command = input.shift();
    }

    if (command == "Done"){
        let spaceLeft = freeSpace - occupiedSpace;
        console.log(`${spaceLeft} Cubic meters left.`)
    }
}

moving(["10",
"1",
"2",
"4",
"6",
"Done"]);