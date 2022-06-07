// DOM Manipulations and Events

/*
1. Creating DOM Elements
- We can create, append and remove HTML elements dynamically;
    - appendChild()
    - removeChild()
    - replaceChild()

- Creating with document.createElement
    - This is called a Factory Pattern
    - Elements are created in memory - they do no exist on the page
    - To become visible, they must be appended to the DOM tree;

- Variables holding HTML elements are live:
    - if you modify the content of the variable, the DOM is updated;
    - if you insert it somewhere in the DOM, the original is moved;

- Text added with textContent will be escaped!
- Text added to innerHTML will be parsed and turned into actual HTML elements
  Beware of XSS attacks!

- appendChild adds a new child as the last child;
- prepend - adds a new child as the first child;

- Deleting DOM Elements:
    - removeChild();
    - remove;
*/

// Creating new DOM element
let p = document.createElement('p');
let li = document.createElement('li');

// Copy DOM element
let liTwo = document.getElementById('my-list');
let newLi = liTwo.cloneNode(true);

// Add to the DOM
document.body.appendChild(liTwo);

// Delete DOM Element
const parent = liTwo.parentElement;
parent.removeChild(liTwo);

/*
2. Browser Events
- Event Objects
    - calls its associated function;
    - passes a single argument to the function - a reference to the event object
    - contains properties that describe the event object:
        - which element triggered the event;
        - screen coordinates where it occured;
        - what is the type of the event;

- Mouse events:
    - click
    - mouseover
    - mouseout
    - mousedown
    - mouseup
- Keyboard events:
    - keydown
    - keypress
    - keyup
- touch events:
    - touchstart
    - touchend
    - touchmove
    - touchcancel
- Focus events:
    - focus (got focus)
    - blur (lost focus)
- DOM/ UI events:
    - load
    - unlioad
    - resize
    - dragstart/ drop
- Form events:
    - input
    - change
    - submit
    - reset
*/

/*
3. Hadnling Events
- Event registration is done by providing a callback function (function passed as parameter)
- Three ways to register for an event:
    - with HTML attribute (onclick..);
    - using DOM element properties;
    - using DOM event hadnler - preferred method

- event.target -> returns the HTML element from the event
- In event handler, this refers to the event source element
- Pay attention when using object methods as event listeners!
- Multiple Listeners:
    - The addEventListener() method also allows you to add many listeners to
      the same element, without overwriting existing ones
*/

// Dom properties
const btn = document.getElementById('btn');
btn.onclick = logEventData;

// Best method
btn.addEventListener('click', logEventData); // Takes two parameters -> event type and callback function
btn.removeEventListener('click', logEventData);

element.addEventListener('click', (e) => {
    console.log(this === e.target); // Always true
});

/*
4. Event Propagation - checks for event listener 
- Capture Phase (From the root to the target)
- Bubbling Phase (from the target to the roots)

- DOM Event Delegation:
    - Allows you to avoid adding event listeners to specific nodes;
    - Event listener is assigned to a single ancestor

- Pros:
    - Simplifies initialization;
    - Saves memory;
    - Less Code
- Cons:
    - Events must be bubbling;
    - May add CPU load;

- stopPropagation() - prevents further propagation of the event;
                    if there are multiple handler for the same event;

- preventDefault() - stops the browser from executing default behavior, eg
                     1. Prevent link from navigating;
                     2. Submitting HTTP requests via forms;
                     3. Prevent default on right click;
*/

document.getElementById('parent-list').addEventListener('click', () => {
    if (e.target && e.target.nodeName == 'LI') {
        console.log(
            'List item',
            e.target.id.replace('post-', ''),
            'was clicked!'
        );
    }
});
