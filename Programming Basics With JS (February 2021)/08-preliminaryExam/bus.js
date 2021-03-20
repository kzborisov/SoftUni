function bus(input) {
    // Read Input
    let passangers = Number(input.shift());
    let busStops = Number(input.shift());

    // Logic

    for (let i = 1; i <= busStops; i++) {
        let leaving = Number(input.shift());
        let getting = Number(input.shift());


        if (i % 2 == 1){
            passangers += 2;  // On every odd stop 2 controls get on.
        } else if (i % 2 == 0) {
            passangers -= 2;
        }
        passangers = passangers - leaving + getting;
    }

    // Print result
    console.log(`The final number of passengers is : ${passangers}`);
}

bus([
"25",
"5",
"14",
"15",
"9",
"11",
"10",
"13",
"6",
"7",
"10",
"8"
]);