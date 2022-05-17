// Lecture 1 - Syntax, Functions and Statements

/*
0. JavaScript Overview
- High-level programming language;
- One of the core technologies of the WWW (JS, HTML, CSS);
- Enables interactive web pages and applications;
- Can be executed on the server and on the client (browser);
- C-like syntax (curly brackets, identifiers, operators);
- Multi-paradigm (imperative, functional, OOP);
- Everything is an object. Objects can have methods and properties;
- Dynamic Typing:
    - operations otherwise done at compile-time can be done at run-time;
    - it is possible to change the type of a variable or add new properties
      or methods to an object while the program is running;
- Node.js:
    - server side JSruntime;
    - Chrome V8 JS engine;
    - NPM package manager;
    - install node packages;
*/

console.log('------------------------ Overview');
let a;
a = 10;
let b = a + 1;

for (let i = 0; i < 10; i++) {
    console.log(i);
}

if (a < 10) {
    console.log('"a" is less than 10');
} else if (a > 10) {
    console.log("'a' is greater than 10");
} else {
    console.log("'a' is equal to 10");
}

function printGreeting() {
    console.log('Hello there!');
}
printGreeting();

/*
1. Data types and variables
- 7 Data types that are primitives (stored in the stack):
    - String    -> 'hello'/ "hello"/ `hello` (interpolated string);
    - Number    -> a numeric data type -> 5/2 => 5.2;
    - Boolean   -> true, false;
    - Undefined -> automatically assigned to variables;
    - Null      -> represents the intentional absence of any object value;
    - BigInt    -> represent integers with arbitary precision;
    - Symbol    -> unique and immutable primitive value;

- Declare Variables:
    - let - allows reassignment (declared in the block scope);
    - var - defines a variable in the
            function scope regardless of block scope (global variables).
            The is no good reasong to use var ever!;
    - const - once assigned it cannot be modified;

- Variables Scope:
    - Global scope variables - not in any block scope;
    - Function scope variables - declared inside of a function;
    - Block scope fucntion - declared inside a pair of curly brackets;

- Functions (method -> function part of a class instance/object):
    - named list of instructions (statements and expressions);
    - can take parameters and return result;
        - naming convention -> cammelCase (classes -> PascalCase);
    - the { stays on the same line as the function declaration;

    - function declaration (they are hoisted, can be accessed before declaring it):
        function walk {}
    - function expression (not hoisted):
        const walk = function (){}
    - arrow function (not hoisted):
        const walk = () => {}

- Parameters and Return Value:
    - you can receive parameters with no value;
    - the unused paramters are ignored;
        function foo(a, b, c){}
        foo(1,2)
        foo(1,2,3,4,5,6)

- Object Methods and Standart Library:
    - method are accessed with the dot-notation;
    - Math, Number, Date, RegExp, JSON;

- Spread operator:
    function myFunc(a, b, c, ...params){} (create params array);
*/

console.log('------------------------ Data Types and Variables');

let myVar = 123n; // n at the end declares BigInt
let mySymbol = Symbol('dsadas'); // Symbol
myVar = 'Hello'; // Not a good practise to change data types

function printStars(count) {
    console.log('*'.repeat(count));
}
printStars(3);

/*
2. Operators and Statements
- Arithmetic Operators (+, - , /, *, %, **);
- Assignment Operators (+=, -=, /=, *=, %=, **=);
- Comparison Operators (==, === (identity operator), !=, !==, >, >=, <, <=)
- Ternary Operator (condition ? return if true : return if false); 
- Truthy and Falsy Values:
    - falsy - false, null, undefined, Nan, 0, 0n, '';
    - truthy - everything else;
- Logical Operators (&&, ||, !):
    - && - returns the leftmost "false" value or the last truthy value if all are true
    - || - returns the leftmost "true" value or the last falsy value if all are false;
-Typeof operator -> returns a string indicating the type of the variable:
    - typeof null -> object;
    - typeoff Nan -> "number";
    - typeof (() => {}) -> function;
    - typeof [1,2,3] -> object (to check if it is array -> Array.isArray([1,2,3]));
- Loops:
    - for
    - for of
    - for in
*/

console.log('------------------------ Operators and Statements');
function largestNumber(first, second, third) {
    console.log(`The largest number is ${Math.max(first, second, third)}.`);
}
largestNumber(2, 1, 3);
const largest = (...p) =>
    console.log(`The largest number is ${Math.max(...p)}.`);
largest(1, 2, 3);

/*
3. Debugging Techniques
- Strict Mode - limits certain "sloppy" language features:
    - 'use strict'; // File-level or function-level;
    - Silent errors will throw Exception instead;
*/

/*
4. Functions and Hoisting
- First-class Functions:
    - a function can be passed as na argument to other functions;
    - can be return by another function and can be assigned as a value to a variable

- Nested Functions:
    - inner functions have acces to variables from their parent;

- Hoisting:
    - variable and function declarations are put into memory during the compile phase,
      but stay exactly where you typed them in your code;
    - only declarations are hoisted;
*/
console.log('------------------------ Functions and Hoisting');
console.log(myHoistedFunct());

function myHoistedFunct() {
    return 'Hoisting my function';
}

let dsadasa = 'dsadsadad';
