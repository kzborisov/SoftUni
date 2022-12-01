function solution() {
    let str = "";

    function append(text) {
        str += text;
    }

    function removeStart(start) {
        str = str.slice(start);
    }
    function removeEnd(end) {
        str = str.slice(0, -end);
    }
    function print() {
        console.log(str);
    }

    return {
        append,
        removeStart,
        removeEnd,
        print,
    };
}

let firstZeroTest = solution();
firstZeroTest.append("hello");
firstZeroTest.append("again");
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();

let secondZeroTest = solution();
secondZeroTest.append("123");
secondZeroTest.append("45");
secondZeroTest.removeStart(2);
secondZeroTest.removeEnd(1);
secondZeroTest.print();
