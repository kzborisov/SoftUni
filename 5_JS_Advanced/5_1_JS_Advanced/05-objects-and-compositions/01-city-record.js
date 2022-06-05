function cityRecord(name, population, treasury) {
    // Syntax sugar, The same as 'name: name'
    return { name, population, treasury };
}

console.log(cityRecord('Tortuga', '7000', '1500'));
