// Task 7 - Cinema Tickets

function cinemaTickets(input) {
    // Read Input
    let movie = input.shift();

    // Logic

    let total = 0;
    let totalStudents = 0;
    let totalStandarts = 0;
    let totalKids = 0;

    while (movie != "Finish"){
        let seats = Number(input.shift());
        let standart = 0;
        let student = 0;
        let kid = 0;
        let totalTickets = 0;

        for (let tickets = 0; tickets <= seats; tickets++){
            totalTickets = standart + student + kid;
            if (totalTickets >= seats){
                break;
            }

            let ticket = input.shift();
            if (ticket === "End") {
                break;
            } else if (ticket === "standard"){
                standart++;
                totalStandarts++;
            } else if (ticket === "student"){
                student++;
                totalStudents++;
            } else if (ticket === "kid") {
                kid++;
                totalKids++;
            }
        }

        console.log(`${movie} - ${((totalTickets / seats) * 100).toFixed(2)}% full.`)
        total += totalTickets;
        
        movie = input.shift();
    }

    // Print result
    console.log(`Total tickets: ${total}`)
    console.log(`${((totalStudents/ total) * 100).toFixed(2)}% student tickets.`);
    console.log(`${((totalStandarts/ total) * 100).toFixed(2)}% standard tickets.`);
    console.log(`${((totalKids/ total) * 100).toFixed(2)}% kids tickets.`);
}

cinemaTickets(["Taxi",
"10",
"standard",
"kid",
"student",
"student",
"standard",
"standard",
"End",
"Scary Movie",
"6",
"student",
"student",
"student",
"student",
"student",
"student",
"Finish"]);