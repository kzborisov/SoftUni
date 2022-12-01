function solution(number) {
    return function (n) {
        return number + n;
    };
}

let add5 = solution(5);
console.log(add5(2));
console.log(add5(3));
