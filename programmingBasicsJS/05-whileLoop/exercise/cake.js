// Task 6 - Cake *

function cake(input) {
    // Read input
    let width = Number(input.shift());
    let length = Number(input.shift());

    // Logic
    let cake = width * length;
    let command = input.shift();
    let totalPieces = 0;

    while (command != "STOP"){
        let currentPiece = Number(command);
        totalPieces += currentPiece;

        if (totalPieces > cake){
            console.log(`No more cake left! You need ${Math.abs(cake - totalPieces)} pieces more.`);
            break;
        }
        command = input.shift();
    }

    if (command == "STOP"){
        console.log(`${cake - totalPieces} pieces are left.`);
    }
}

cake(["10",
"2",
"2",
"4",
"6",
"STOP"]);