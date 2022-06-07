// Advanced Functions

/*
1. Execution Context
- the function context is the object that owns the currently executed code;
- function context === 'this' object;
- depends on how the function is called:
    - global invoke: func();
    - object invoke: object.function();
    - DOM event: element.addEventListener()
    - using call()/ apply() / bind(); - we choose what 'this' points to;
        - explicit binding;
        - forces a function call to use a praticular object for this binding;

- Inner method context - 'this' is accessible only by the outer method
                         nested functions cannot access it;

- Arrow function context - this retains the value of the enclosing lexical context ,we cannot change it;

*/

function printContext(a, b) {
    console.log(a + b);
    console.log(this);
}

printContext(3, 5); // gloval in the console, window in the browser

const obj = {
    counter: 5,
    printContext,
};

obj.printContext(3, 5); // Reference to the obj

// el.addEventListener('click', printContext); // Referrence to the button

const newObj = {
    counter: 10,
};

printContext.apply(newObj, [2, 3]); // Referrence to newObje
printContext.call(newObj, 2, 3); // Referrence to newObje
const boundFunc = printContext.bind(newObj);
boundFunc(1, 2);

const func = () => console.log(this);
func(); // {} instead of global;

const arrObj = {
    name: 'Peter',
    method() {
        const func = () => console.log(this);
        func();
    },
};

arrObj.method(); // Binds the object to the function;

/*
2. Functional Programming in JS
- First-class functions are treated like any other variables;
    'The term first-class means that something is just a value.
     A first-class function is one that can go anywhere that any
     other value can go - there are a few to no restrictions'
    - passed as an argument;
    - returned by another function;
    - assigned as a value to a variable;

- Higher order functions - take other functions as an argument or return a function
                           as result;

- Predicates - any functions that returns a Boolen
             - Predicates are often found in the form of callbacks;

- Build-it Higher order functions:
    - Array.prototype.map
    - Array.prototype.filter
    - Array.prototype.reduce
    - Array.prototype.some
    - Array.prototype.every

- Pure functions - return the same result given the same parameters;
                 - execution is independent of the state of the system;

- Referential Transparency - an expression that can be replaced with its corresponding
                             value without changing the program's behavior;
                           - Expression is pure and its evaluation mist have no side effects;
*/

function createExecutor(func, text) {
    const str = func();
    return printResult;

    function printResult() {
        console.log(str, text);
    }
}

const myFunc = () => 'hello';
const executor = createExecutor(myFunc, 'world!');
executor();

// Referential Transparency
const add = (a, b) => a + b;
const mult = (a, b) => a * b;

console.log(add(2, mult(3, 4))); // mult(3, 4) can be replaced with 12

/*
3. Closure
- one of the most important features in JavaScript;
- the scope of an inner function includes the scope of the outer function;
- an inner function retains variables being used from the outer function scope
  even after the parent function has returned;
- an inner function retains variables being used from the outer function scope
  even after the parent function has returned;
- a state is preserved in the outer function (CLOSURE!);

- IIFE (LEGACY) - Immediately-Invoked Function Expressions
    - Define anonymous function expression;
    - Invoke it immediately after declaration;
    - Prevents poluting the scope, deprecated after the introduction of let and const;
*/

function start() {
    let counter = 0; // Counter is only visible inside the start function!

    function increment(n) {
        counter += n;
        console.log(counter);
    }

    return increment;
}

const myCounter = start();
myCounter(1);
myCounter(1);
myCounter(1);

// IIFE - Legacy
(function () {
    let name = 'Peter';
    console.log(name);
})();

/*
4. Function Decoration
- Partial Application:
    - Set some of the argument of a function, without executing it;
    - Pass the remaining arguments when a result is needed;
        - the partially applied function can be used multiple times;
        - it will retain all fixed arguments, regardless of context;

- Currying (named by Haskle Curry):
    - technique for function decomposition;
    - supply arguments one at a time, instead of at once;
    - they may come from different source;
    - execution can be delayed until it's meeded;
    - Usage:
        - Function Composition - building new function from old funtion by passing
                                 arguments;
        - Memoization - Functions that are called repeatedly with the same set of inputs
                        but whose result is relatively expensive to produce;
        - Handle Errors - Throwing functions and exiting immediately after an error;

- Currying vs Partial:
    - Cyrrying always produces nested unary functions (one argument)
    - Partial application produces functions of arbitary number of arguments;
    - Currying in NOT partial application:
        - it can be implemented using partial application;
*/

// Partial Application
const f = (x, y) => x + y;
const g = (x) => f(1, x);

console.log(g(5));

const sqr = (x) => Math.pow(x, 2);
console.log(sqr(2));

// Currying
function sum3(a) {
    return (b) => {
        return (c) => {
            return a + b + c;
        };
    };
}

console.log(sum3(5)(6)(8));
