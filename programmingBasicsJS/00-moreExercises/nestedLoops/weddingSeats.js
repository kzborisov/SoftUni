// Task 6 - Wedding Seats

function weddingSeats(input) {
    // Read Input
    let lastSector = input.shift();
    let firstSectorRows = Number(input.shift());
    let oddRowSeatsCount = Number(input.shift());

    // Logic
    let sectorStart = 'A'.charCodeAt(0);
    let sectorEnd = lastSector.charCodeAt(0);

    let seatStart = "a".charCodeAt(0);

    let counter = 0;

    // Sectors
    for (let sector = sectorStart; sector <= sectorEnd; sector++) {
        for (let row = 1; row <= firstSectorRows; row++) {
            if (row % 2 != 0) {
                for (let seat = seatStart; seat < seatStart + oddRowSeatsCount; seat++) {
                    console.log(`${String.fromCharCode(sector)}${row}${String.fromCharCode(seat)}`);
                    counter++;
                }
            } else {
                for (let seat = seatStart; seat < seatStart + oddRowSeatsCount + 2; seat++) {
                    console.log(`${String.fromCharCode(sector)}${row}${String.fromCharCode(seat)}`);
                    counter++;
                }
            }
        }
        if (firstSectorRows + 1 > firstSectorRows){
            firstSectorRows++;
        }
    }
    console.log(counter);
}

weddingSeats(["B", "3", "2"]);