function solve(input) {
    let result = [];

    const processor = {
        add: (str) => result.push(str),
        remove: (str) => (result = result.filter((item) => item !== str)),
        print: () => console.log(result.join(",")),
    };

    input.forEach((elem) => {
        const [cmd, text] = elem.split(" ");
        processor[cmd](text);
    });
}

solve(["add hello", "add again", "remove hello", "add again", "print"]);
