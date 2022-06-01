// 1. Arrays And Nested Arrays

/*
0. Arrays
- List-like objects
- Arrays are a reference type, the variable points to an address in memory
    *Refference type:
        not stored in the stack (declares scopes and variables),
        but a refference to the address in the memory;
        they are compared by reference;
- Elements are numbered from 0 to length - 1;
- Creating an array using an array literal - myArr = [1,2,3];
- Neither the length nor the types of its element's are fixed;
- Data can be stored at non-contiguous locations in the array;
- JS arrays are not guaranteed to be dense (sparse array);
- Not a good practise to have mixed data in the array;
- Accessing indexes out of range returns "undefined";
- It's considered an error to use invalid indexes (<0, strings, etc.)

Dirty hack - not part of the array, not a good practise
cars["hidden"] = "Hacker"; // Create "hidden" property
console.log(cars.hidden);
*/

console.log('------------------------ Arrays');
const myArr = [10, 20, 30, 40, 50];
console.log(myArr[2]); // Accessing array elements
console.log(myArr.length); // Return the length of the array
console.log(myArr[myArr.length - 1]); // Last element of the array
myArr[7] = 101; // Setting element outside of the range of the array
console.log(myArr);

// For of loop
for (const el of myArr) {
    console.log(el);
}

// For loop
for (let index = 0; index < myArr.length; index++) {
    const element = myArr[index];
    console.log(element, index);
}

/*
1. Accessing Array Elements 
- Destructuring Syntax:
    - expression that unpacks values from arrays or objects, into distinct variables;
- Rest operator - takes elements and puts them in an array;
- Spread operator - takes an array and gets its values;
*/

console.log('------------------------ Accessing Arrays');
let numbers = [1, 2, 3, 4];
let [...copy] = numbers; // Create shallow copy of the array
let [a, b, ...elems] = numbers; // Destructuring, ...elems -> rest operator
console.log(...numbers); // Spread operator

/*
2. Mutator Methods
- pop() - remove the last element of the array and returns it;
- push() - adds element at the end of the array;
    - Push and pop makes the arrays a stack;
- shift() - Remove the first element and removes it;
- unshift() - Adds element at the start of the array;
    - Unshift and pop makes the array a queue;
- splice(index, numOfElements, elementsWeWantToAdd) - Changes the contents
    of an array by removing or replacing ex;isting elements and/or adding
    new elements
-fill() - fills all the elements of an array from start index to and end index with static values;
- reverse() - reverses the array; 
- sort(), providing a compare function
    - by default compares as strings (ASCII)
    - length < 22 -> insertion sort
    - length > 22 -> merge sort, radix sort etc.
*/

console.log('------------------------ Mutator methods');
console.log(myArr.pop());
console.log(myArr.push(50));
console.log(myArr.unshift(60));
console.log(myArr.shift());
console.log(myArr.splice(1, 1)); // Removes the element on the first index and returns it
console.log(myArr.splice(2, 0, ...[21, 22, 23])); // Adds 21, 22, 23 starting from index 2
console.log(myArr.splice(2, 3, 25)); // Replaces the element at index 3 with 25
const arr = [1, 7, 2, 5];
console.log(arr);

// Sorting Numbers
arr.sort((a, b) => a - b);
console.log(arr);

// Sorting Strings
const names = ['Ann', ' George'];
names.sort((a, b) => a.localeCompare(b)); // Ascending
names.sort((a, b) => b.localeCompare(a)); // Descending

function compare(a, b) {
    if (a > b) {
        return 1;
    } else if (b > a) {
        return -1;
    } else {
        return 0;
    }

    // Simpler solution
    return a - b; // Ascending
    // return b - a; // Descending
}
/*
3. Accessor Methods
- join - returns string, separting elements by provided separator (space by default)
- concat - merges two or more arrays;
- slice - returns a shallow copy of a portion of an array into a new array;
- includes - Check if an array contains element, returns a Bolean;
- indexOf - return the first index at which a given element can be found
            return -1 if element is not found;
*/

console.log('------------------------ Accessor Methods');
let fruits = ['banana', 'orange', 'lemon'];
console.log(fruits.slice(0, 2)); // Negative indexes start from the end of the array
console.log(fruits.includes('banana'));

/*
4. Iteration Methods
- forEach - takes a function as parameter;
- map - creates a new array with the results of calling a provided function on
        each element in the calling array;
- some - method tests whether at least one el in the array passes the test 
         implemented by the provided function;
- every - all elements pass the test;
- find - returns the first element in the array, if an element in the array satisfies
         the provided testing function or undefined if not found;
- filter - creates a new array with filtered elements
*/
console.log('------------------------ Iteration Methods');
fruits.forEach((x) => console.log(x));

const numsAsStr = ['10', '21', '30', '40'];
const nums = numsAsStr.map((x) => Number(x)); // numsAsStr.map(Number)
console.log(nums);

console.log(nums.some((x) => x >= 22));

console.log(nums.every((x) => x >= 22));

console.log(nums.find((x) => x >= 22));

console.log(nums.filter((x) => x >= 22));

/*
5. The reduce() Method 
- executes a reducer function on each element of the array,
  resulting in a single output value;
-  takes 2 parameters - 1 reducer function, accumulator
*/
const result = nums.reduce(reducer, 0);
console.log(result);

function reducer(accumulator, value) {
    return accumulator + value;
}

const resultTwo = nums.reduce((a, v) => a + v, 0);
console.log(resultTwo);

/*
6. Nested Arrays
*/
