// Task 6 - Building

function building(input) {
    // Read Input
    let storyCount = Number(input.shift());
    let roomsCount = Number(input.shift());

    // Logic
    for (let story = storyCount; story >= 1; story--) {
        let type = "";
        if (story % 2 === 0 && story != storyCount){
            type = "O";
        }
        else if (story % 2 != 0){
            type = "A";
        }

        if (story === storyCount){
            type = "L";
        }
        for (let room = 0; room < roomsCount; room++) {
            process.stdout.write(`${type}${story}${room} `);
            
        }
        console.log();
    }
}

building(["9", "5"]);