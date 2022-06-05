function townPopulation(input) {
    const result = {};

    for (const town of input) {
        const tokens = town.split(' <-> ');
        const name = tokens[0];
        let population = Number(tokens[1]);

        if (result[name] != undefined) {
            population += result[name];
        }
        result[name] = population;
    }

    for (const town in result) {
        console.log(`${town} : ${result[town]}`);
    }
}

townPopulation([
    'Istanbul <-> 100000',
    'Honk Kong <-> 2100004',
    'Jerusalem <-> 2352344',
    'Mexico City <-> 23401925',
    'Istanbul <-> 1000',
]);
