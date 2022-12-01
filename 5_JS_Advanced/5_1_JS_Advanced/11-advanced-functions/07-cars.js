function solve(input) {
    const cars = {};
    const processor = {
        create,
        set,
        print,
    };

    function create(name, inherits, parent) {
        cars[name] = inherits ? Object.create(cars[parent]) : {};
    }

    function set(name, key, value) {
        cars[name][key] = value;
    }

    function print(name) {
        const props = [];
        for (const key in cars[name]) {
            props.push(`${key}:${cars[name][key]}`);
        }
        console.log(props.join(","));
    }

    input.forEach((elem) => {
        const [cmd, name, opt, value] = elem.split(" ");
        processor[cmd](name, opt, value);
    });
}

solve([
    "create c1",
    "create c2 inherit c1",
    "set c1 color red",
    "set c2 model new",
    "print c1",
    "print c2",
]);
