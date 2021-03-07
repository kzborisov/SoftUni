// Task 7 - School Camp

function truckDriver(input) {
    // Read Input Data
    let season = input[0];
    let groupType = input[1];
    let childrenCount = Number(input[2]);
    let nightsCount = Number(input[3]);

    // Logic
    let priceMap = {
        'girls': {
            'Winter': 9.60,
            'Spring': 7.20,
            'Summer': 15
        },
        'boys': {
            'Winter': 9.60,
            'Spring': 7.20,
            'Summer': 15
        },
        'mixed': {
            'Winter': 10,
            'Spring': 9.50,
            'Summer': 20
        }
    };

    let sportMap = {
        'girls': {
            'Winter': 'Gymnastics',
            'Spring': 'Athletics',
            'Summer': 'Volleyball'
        },
        'boys': {
            'Winter': 'Judo',
            'Spring': 'Tennis',
            'Summer': 'Football'
        },
        'mixed': {
            'Winter': 'Ski',
            'Spring': 'Cycling',
            'Summer': 'Swimming'
        }
    };

    let sport = sportMap[groupType][season];
    let sum = priceMap[groupType][season] * childrenCount * nightsCount;
    if (childrenCount >= 50) {
        sum *= 0.50;
    } else if (childrenCount >= 20) {
        sum *= 0.85;
    } else if (childrenCount >= 10) {
        sum *= 0.95;
    }

    // Print Result
    console.log(`${sport} ${sum.toFixed(2)} lv.`)
}

truckDriver(["Summer", "boys", "60", "7"])