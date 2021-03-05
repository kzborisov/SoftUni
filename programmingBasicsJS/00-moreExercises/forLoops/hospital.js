// Task 2 - Hospital

function hospital(input) {
    // Read Input
    let days = Number(input[0]);

    let doctors = 7;
    let treated = 0;
    let untreated = 0;

    // Logic
    for (let i = 1; i<=days; i++) {
        if (i % 3 === 0 && untreated > treated) {
            doctors++;
        }

        let patients = Number(input[i]);

        if (patients < doctors){
            treated += patients;
        } else {
            treated += doctors;
            untreated += patients - doctors;
        }
    }

    // Print Result
    console.log(`Treated patients: ${treated}.`);
    console.log(`Untreated patients: ${untreated}.`);
}

hospital(["6", "25", "25", "25", "25", "25", "2"]);