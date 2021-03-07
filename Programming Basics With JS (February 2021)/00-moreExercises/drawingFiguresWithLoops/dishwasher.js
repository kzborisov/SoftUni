// Task 1 - Rectangle 10 x 10 *

function dishwasher() {
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 10; j++) {
            process.stdout.write("*");
        }
        console.log('');
    }
}

dishwasher()