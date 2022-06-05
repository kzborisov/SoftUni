function cityTaxes(name, population, treasury) {
    // Factory functions
    const result = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += Math.floor(this.population * this.taxRate);
        },
        applyGrowth(percent) {
            this.population += Math.floor((this.population * percent) / 100);
        },
        applyRecession(percent) {
            this.treasury -= Math.floor((this.treasury * percent) / 100);
        },
    };

    return result;
}

// Kind of like constructor
const city = cityTaxes('Tortuga', 7000, 15000);

console.log(city);
