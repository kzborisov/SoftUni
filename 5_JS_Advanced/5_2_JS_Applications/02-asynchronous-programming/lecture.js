/*
1. AJAX (Asynchronous JavaScript and XML)
- background loading of dynamic content/data
- load data from the Web server and render it
*/

/*
2. Synchronous vs Asynchronous
2.1 Async
- Structured using callback functions;
- in current versions of JS there are:
    - callbacks
    - promises
    - async functions
! Not the same thing as a concurrent or multi-threaded
- JS code is generally single-threaded

- runs several tasks in parallel, at the same time;

2.2 Callbacks
- function passed into another function as an argument;
- then invoked inside the outer function to complete some kind of routine or actions

*/

/*
3. Promises
- A promise is an asynchronous action that may complete at some point and produce a value
- States:
    - pending - operations still running
    - fulfilled - operation finished
    - failed - operation failed

- Promises use the Promise class:
    new Promise(executor);

Promise Methods:
    - Promise.then()
    - Promise.catch()
    - Promise.reject(reason) - returns an object that is rejected with the given reason
    - Promise.resolve(value) - returns an object that is resolved with the given value
    - Primise.all(iterable) - returns a promise, fulfills when all of the promises have fulfilled, rejects as soon as on of them rejects
    - Promise.allSettled(iterable) - wait until all promises have settled
    - Promise.race(iterable) -  returns a promise that fulfills or rejects as soon as one of the promises in an iterable is settled
    - Promise.prototype.finally() - the handler is called when the promise is settled

What is Fetch?
- the fetch() method allows making network requests
- it is similar to XMLHttpRequest (XHR). The main difference is that the Fetch API:
    - uses promises;
    - enable as simpler and cleaner API
    - makes code more readable and maintainable
    - the response of a fetch() request is a Stream object
    - the reading of the stream happens asynchronously
    - when the json() method is called, a Promise is returned:
        - the response status is checked (should be 200) before parsing the response as JSON

GET Request:
- Fetch API uses the GET method so that a direct call would be like this:
    fetch('<api url>')
        .then(r => r.json())
        .then(data => console.log(data))
        .cathc(error => console.log(error))

POST Request:
- To make a POST request, we can set the method and body parameters in the fetch() options:
    fetch('/url', {
        method: 'post',
        headers: { 'Content-Type': 'applicaiton/json' },
        body: JSON.stringify(data),
    })

Body Methods:
- clone() - create a clone of the response
- json()  - resolves the promise with JSON
- redirect() - create new promise but with different URL
- text()  - resolves the promise with string
- arrayBuffer() - resolve body with ArrayBufer
- blob() - resolve body with Blob (file, image, etc)
- formData() - resolve body with FormData

Response Types:
- basic - normal, same origin response;
- cors - response was received from a valid cross-origin request
- error - error network
- opaque - response for "no-cors" request to cross-origin resource
- opaqueredirect - the fetch request was made with redirect: "manual"

Chaining Promises:
- when working with a JSON API, you can:
    - define the status and JSON parsing in separate functions
    - the functions return promises which can be chained
*/

/*
4. Async/Await
- Async functions
    - returns a promise, that can await other promises in a way that looks synchronous
    - operate asynchronously via the event loop
    - contains an wait expression that:
        - is only valid inside async functions
        - pauses the execution of that function
        - waits for the promise's resolution

async function asyncCall(){
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

Do not confuse await with Promise.then()!
- await is always used for a single promise
- to await two or more promises in parallel, use Promise.all();

- If a promise resolves normally, then await promise returns the result:
- In case of a rejection, it throws an error;

Promise.then():
function logFetch(url){
    return fetch(url)
        .then(r => r.text())
        .then(text => console.log(text))
        .catch(err => console.log(error))
}

Async/Awaiit
async function logFetch(url){
    try{
        const response = await fetch(url);
        console.log(await response.text());
    }
    catch(err) {
        console.log(err);
    }
}

async function f(){
    let response = await fetch();
}
f.catch(alert);

To execute different promise methods one by one, use Async/Await
*/
