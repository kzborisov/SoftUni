// Task 4 - Metric Converter

function metricConverter(input) {
    // Read Input Data
    let numToConvert = Number(input[0]);
    let inputMetric = input[1];
    let outputMetric = input[2];

    let result;

    // Calculations
    let dictMap = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0
    };

    result = numToConvert * dictMap[inputMetric] / dictMap[outputMetric]

    // Print result
    console.log(result.toFixed(3));
}

metricConverter(["45","cm","mm"]);