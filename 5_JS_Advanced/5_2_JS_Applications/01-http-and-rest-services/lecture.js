/*
1. HTTP Basics
- HTTP - Hyper Text Transfer Protocol
    - text-base client-server protocol for internet;
    - for transfering Web resources (HTML file, images, styles, etc);
    - request-response based

1.1 HTTP Request Methods:
- HTTP defines methods to indicate the desired action to be performed on the identified resource:
    - GET     - retriev/load a resource;
    - POST    - create/store a resource;
    - PUT     - update a resource;
    - DELETE  - delete(remove) a resource;
    - PATCH   - update resource partially;
    - HEAD    - retrieve the resource's headers;
    - OPTIONS - returns the HTTP methods that the server supports for the specified URL;

1.2 HTTP Response Status Codes:
- 200 - OK
- 201 - Created
- 204 - No Content
- 301/302 - Moved
- 400 - Bad Request
- 401/403 - Unauthorized
- 404 - Not Found
- 409 - Conflict
- 500/503 - Server Error

- The Content-Type/Content-Disposition headers specify how the HTTP request/response body should be processed;
*/

/*
2. REST and RESTful Services
- Representational State Transfer (REST)
    - Architecture for client-server communication over HTTP
    - resources have URI (address)
    - can be created/retrieved/modified/deleted/etc.

- RESTful API/RESTful Service
    - provides access to server-side resources via HTTP and REST;

- REST defines 6 architectural constraints which make any web service a true RESTful API
    - client-server architecture;
    - statelessness;
    - cacheable;
    - layered system;
    - code on demand (optional);
    - uniform interface;
*/

/*
3. BaaS (Back-end as a Service)
- Web applicaitons require a back-end to store information (user profiles, setting, content, etc)
- Creating a back-end can be very time consuming;
- Ready to use back-end services are available (Firebase, Backendless, Back4App, etc) 
*/
