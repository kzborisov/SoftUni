function circleArea(radius) {
    let radiusType = typeof radius;

    if (radiusType !== "number") {
        console.log(
            `We can not calculate the circle area, because we receive a ${radiusType}.`
        );
        return;
    }

    let result = radius ** 2 * Math.PI;
    console.log(result.toFixed(2));
}

circleArea(5);
