// Task 7
// Calculate the necessary hours for an architect to finish
// His project.
function calculateTime(input) {
    let name = input[0];
    let projects = Number(input[1]);
    let hoursForProject = 3;
    let hours = projects * hoursForProject;
    console.log(`The architect ${name} will need ${hours} hours to complete ${projects} project/s.`)
}

calculateTime(["George", "4"]);