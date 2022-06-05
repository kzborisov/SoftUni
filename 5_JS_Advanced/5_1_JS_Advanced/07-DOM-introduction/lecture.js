// DOM Introduction - Document Object Model

/*
1. Browser API
- Browse Object Model
- Broweser expose some objects like window, screen, navigator,
  history, location, document,
- The global object in the browser is "window" (this === window);
  */
window.location;
window.history;
document;

/*
2. Document Object Model
- The DOM represent the document as nodes and objects;
- That way the programming language can connect to the page;
- The HTNL DOME is an Object Model for HTML. It defines:
    - HTML elements as objects;
    - Properties;
    - Methods;
    - Events;
- The broweser parses HTML and creates a DOM Tree;
- The elements are nested in each other and creates a hierarchy;
    - Like the hierarchy of a street address - Coutry, City, Street
- Dom Methods - actions you can perform on HTML elements;
- DOM Properties - values of HTML elements that you can set or change;
- HTML DOM method is and you can do (like add or delete an HTML element);
- HTML DOM property is a value that you can get or set (changing the content of an HTML element);
- JavaScript can interact with web pages via the DOM API;
    - Check the contents and structure of elements on the page;
    - Modify element style and properties;
    - Read user input and react ot events;
    - Create and remove elements;
- Most actions are performed when an event occurs:
    - events are "fired" when something of interest happens;
- Static elemetns have textContent and innerHtml;
- Dynamic elements have value;
- Code can be executed in the page in different ways:
    - directly in the developer console - when debugging;
    - as a page event handler - e.g user clicks on a button (onclick="...");
    - Via inline script, using the <script> tag (Global scope - window object);
    - By importing from external file - most flexible method;
*/

temp0.textContent; // The text of an HTML element;
temp0.innerHTML; // The html of the elements;
temp0.value; // The value of an input fields;
temp0.style; // Change the css style

/*
3. HTML Elements
- The DOM Tree is comprised of HTML Elements;
- Elemets are JS objects with properties and methods:
    - Then can be accessed and modified like regular objects;
- To chang ethe contents of the page:
    - Select an element to obtain a reference;
    - Modify its properties;

- Attributes are defined by HTML:
    - Attributes initializa DOM properties;
    - Property values can change via the DOM API;
- The HTML attribute and the DOM property are techically not the same thing;
- Since the outcome is the same, in practise you will almost never encounter a differemce;

- DOM Manipulations:
    - The HTML DOM allows JS to change the content of HTML elements
*/

innerHTML;
textContent;
value;
style;

/*
4. Targeting Elements (Selecting)
- Ways to find a certain HTML elements in the DOM:
    - By ID - getElementById() -> Only one;
    - By classname - getElementsByClassName() -> collection;
    - By tag name - getElementsByTagName() -> collection;
    - By query selector (Return NodeList):
        querySelector() -> only the first match;
        querySelectorAll() -> collection;

- Css selectors:
    - #main - returns element with ID main;
    - #content div -> select all divs inside the element with ID content;
    - .note, .alert -> all elements with class "note" or "alert";
    - input[name='login'] -> input with name 'login';

- Node List vs HTMLCollection:
    - Both interfaces are collection of DOM nodes;
    - NodeList can contain any node type, including text and whitespace;
    - HTMLCollection contains only Element nodes;
    - Both have iteration methods, HTMLCollection has an extra namedItem method;
    - HTMLCollection is live while NodeList can be either live or static; 

- NodeList and HTMLCollections are NOT arrays;
- They can be indexed and iterated (for...of);
- Both can be explicitly converted to an array -> Array.from(elements);

- Parents and Child Elements:
    - every DOM element has a parent;
        - parents can be accessed by property "parrentElement" or "parrentNode";
    - When some element contains other elements, that mease he is parent of those elements;
    - They are childre to the parent. Then can be accessed by the property "children"
*/

const list = document.querySelector('ul');
const col = list.children; // HTMLCollection with all li elements inside the ul

const li = document.querySelector('li');
const ul = li.parentElement; // ul

/*
5. Using the DOM API
- functions from script files are in the global scope;
- can be referenced and executed from events and inline scripts;
- multiple script files in a page can see each other;
- pay attention to load order!
- Content can be hidden or revealed by changing its display style:
    - This is a commont technique to display content dynamically;

*/
const element = document.getElementById('main');
element.style.display = 'none'; // Hide an element;
element.style.display = 'block'; // Reveal an element
