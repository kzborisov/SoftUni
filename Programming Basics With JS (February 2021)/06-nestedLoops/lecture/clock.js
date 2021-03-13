// Task 1 - Clock

function clock() {
    for (var hour = 0; hour < 24; hour++){
        for (var minutes = 0; minutes < 60; minutes++){
            console.log(`${hour}:${minutes}`)
        }
    }
}

clock()