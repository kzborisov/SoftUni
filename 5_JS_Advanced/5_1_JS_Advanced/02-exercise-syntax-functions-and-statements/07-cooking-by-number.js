function cookingByNumber(num, ...args) {
    let result = parseInt(num);

    for (const operation of args) {
        switch (operation) {
            case 'chop':
                result *= 0.5;
                break;
            case 'dice':
                result = Math.sqrt(result);
                break;
            case 'spice':
                result += 1;
                break;
            case 'bake':
                result *= 3;
                break;
            case 'fillet':
                result *= 0.8;
                break;
        }
        console.log(result);
    }
}

cookingByNumber('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cookingByNumber('9', 'dice', 'spice', 'chop', 'bake', 'fillet');
