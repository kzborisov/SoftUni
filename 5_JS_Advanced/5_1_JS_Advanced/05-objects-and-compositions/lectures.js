// Objects And Composition

/* 
1. Objects in JavaScript
- collection of fields, called properties;
- a propertiy is an association between a name (key) and a value;
- objects are a reference data type
- in JS they are created with an object literal {}

1.1 Object properties:
    - a property of an oject can be explained as a variabel that is attached to the object;
    - object properties are the same as oridinary variables,
      and can hold any data type and be reasigned;

1.2 Destructuring:
    - can be used to get multiple property values

1.3 Deleteing property:
    - delete person.age
1.4 Object References:
    - variables holding reference data types contain the memory address
      of the data;
    - Copies of the refenrec point to the same data;

1.5 Comaprinng Objects:
    - two variables, two distinct objects with the same properties;
*/

const person = {
    firstName: 'John',
    lastName: 'Doe',
    age: 50,
};

person.firstName = 'Peter';
person.newProp = 'new property';

console.log(person);
console.log(person.firstName);
console.log(person['age']);

const { firstName, age } = person;
console.log(firstName, age);

delete person.newProp;
console.log(person);

/* 
2. Objects as Associative Arrays
- Dict in Python;
- Objects can serve the role of associative arrays in JS;
    - the keys are string indexes;
    - values are associated to a key;
    - all values should be of the same type;
    - key-value pairs

- for...in Loop: 
    - iterates over all enumerable properties;
- Object.keys -> return all the keys;
- Object.values -> return all values;
- Object.entries -> returns an array of tuples representing each key and values pair;
                    (Often used for sorting)
*/

const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
    console.log(key, obj[key]);
}

/* 
3. Methods and Context
- Object can also have method;
- They are actions that can be performed on objects;
- Methods are stored in properties as function definitions;
- Related functions may be grouped in an object;
- The object serves as a function library (Math, Object, Number, etc.)
- Use Named Methods instead of switch;

- Functions in JS have execution context
    - accessed with the keyword 'this' (the instance) - self in python;
    - when executed as an object method the context is a refenrce to
      the parent object;
    - context can be changed at runtime;
    - if a function is executed outside of its parent object,
      it will no longer have access to the object's context;
*/

const newPerson = {
    firstName: 'John',
    lastName: 'Doe',
    age: function (myAge) {
        return `My age is ${myAge}!`;
    },
    fullName() {
        // Context
        return this.firstName + ' ' + this.lastName;
    },
};

console.log(newPerson.age(21));
console.log(newPerson.fullName());

// Replace switch
let count = 5;
const parser = {
    increment() {
        count++;
    },
    decrement() {
        count--;
    },
    reset() {
        count = 0;
    },
};
parser['increment']();
console.log(count);

/* 
4. Object Compositions
- Combining simple object into more complex ones;
- powerful technique for code reuse;
- It can be considered superior to OOP inheritance;
- We can compose behavior at run-tim and reuse functionality;
- Describe objects in terms of what they do, not what they are;
- This solves a deeply rooted problem with OOP inheritance;
- Can solve the deadly dimond (Multiple Inheritance) problem;

- Factory Functions with reference
    - functions that compose and return objects
    - creating method with object reference can avoid the pitfalls
      of using 'this';

- Decorator Functions:
    - Functions that add new data and behaveior to objects
*/
const student = {
    firstName: 'John',
    lastName: 'Doe',
    age: 22,
    location: { lat: 42.698, lng: 23.322 },
};

console.log(student.location.lat);

function print() {
    console.log(`${this.name} is printing a page`);
}

function scan() {
    console.log(`${this.name} is scaning a page`);
}

const printer = {
    name: 'ACME Printer',
    print,
};
const scaner = {
    name: 'Initech Scanner',
    scan,
};

const copier = {
    name: 'ComTron Copier',
    print,
    scan,
};

// Factory function
function createRect(width, height) {
    const rect = {
        width,
        height,
    };

    rect.getArea = () => {
        return rect.width * rect.height;
    };
    return rect;
}

// Decorator Functions
function canPrint(device) {
    device.print = () => {
        console.log(`${device.name} is printing a page`);
    };
}
const p = { name: 'ACME Printer' };
canPrint(p);
p.print();
/* 
5. JSON
- JavaScript Object Notation;
- It's data interchange format
- It's language independent - syntax like JavaScript object syntax,
  but the JSON format is text only
- key/value pairs,
- separated by commas,
- JSON only takes double quotes
- JSON.parse() -> to convert the JSON format into a JS object;
- JSON.stringyfy() -> to convert objects into a string
*/

let data = '{ "manager": {"firstName": "John", "lastName": "Doe"} }';
let o = JSON.parse(data);
console.log(o.manager.firstName);

let newObj = { name: 'John', age: 30 };
let myJSON = JSON.stringify(newObj);
console.log(myJSON);
