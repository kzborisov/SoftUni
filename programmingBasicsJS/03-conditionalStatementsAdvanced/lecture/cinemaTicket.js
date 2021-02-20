// Task 8 - Cinema Ticket

function cinameTicket(input) {
    // Read Input Data
    let day = input[0];

    // Calculations
    let ticketMap = {
        "Monday": 12,
        "Tuesday": 12,
        "Wednesday": 14,
        "Thursday": 14,
        "Friday": 12,
        "Saturday": 16,
        "Sunday": 16
    };

    // Print Result
    console.log(ticketMap[day])
}

cinameTicket((["Sunday"]));
