function roadRadar(speed, area) {
    let speedLimitsMap = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20,
    };

    speedDifference = speedLimitsMap[area] - speed;
    let exessiveSpeed = Math.abs(speedDifference);
    let status =
        exessiveSpeed > 40
            ? 'reckless driving'
            : exessiveSpeed > 20
            ? 'excessive speeding'
            : 'speeding';

    if (speedDifference >= 0) {
        console.log(`Driving ${speed} km/h in a ${speedLimitsMap[area]} zone`);
    } else {
        console.log(
            `The speed is ${exessiveSpeed} km/h faster than the allowed speed of ${speedLimitsMap[area]} - ${status}`
        );
    }
}

roadRadar(40, 'city');
roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');
