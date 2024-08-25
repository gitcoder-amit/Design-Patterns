'''

what is rest api --> rest stands for representational state transfer and rest api is a web base api(application programming interface that follows rest architetural style). The primary purpose of rest is to provide an architecture for builing web services that can be consumed by various clients including web, mobile and desktop applications. Rest is based on HTTP which is the standard protocol used for communication on the internet. It uses the HTTP method including get, post, put, patch, delete etc to perform various operations on the resources each resource in rest is identified by unique url. and the response is returned in JSON, XML, text, or CSV format. Essencial feature of rest api is it follows the stateless client server architecture model which means server doesn't need to store any information about the client's state between requests, instead each request contains all necessary information required by the server to process the request. This architecture makes rest api scalable and easy to maintain.

When to use REST API?
   Rest api is an excellent choise when building web services that require a stateless, scalable  and easy to maintain architecture
   It's ideal for building web application that require crud operations such as creat, read, update, delete data. Rest API is also suitable for building applications that require real time communication such as chat application.add()


1. What is REST?
Answer: REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- the HTTP protocol is typically used. RESTful applications use HTTP requests to perform CRUD operations on resources, which are identified by URLs.

Example: A RESTful web service could expose endpoints like:

GET /users - Retrieve a list of users
POST /users - Create a new user
GET /users/{id} - Retrieve a specific user by ID
PUT /users/{id} - Update a user by ID
DELETE /users/{id} - Delete a user by ID


2. What are the principles of REST?
Answer: The main principles of REST are:

Stateless: Each request from client to server must contain all the information needed to understand and process the request.
Client-Server: Separation of concerns between client and server.
Cacheable: Responses must be defined as cacheable or non-cacheable to improve performance.
Uniform Interface: Resources are manipulated through a common interface using standard HTTP methods.
Layered System: A client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary along the way.


3. What is a resource in REST?
Answer: A resource is an object or representation of something that is accessible via a unique URI. Resources are the fundamental units in REST.

Example: In a RESTful service managing users, a user object would be a resource. A user could be accessed via /users/{id} where {id} is the unique identifier for the user.



4. What HTTP methods are commonly used in RESTful services?
Answer: The common HTTP methods used in RESTful services are:

GET: Retrieve a resource.
POST: Create a new resource.
PUT: Update an existing resource.
DELETE: Delete a resource.
PATCH: Partially update a resource.
Example:

GET /products - Retrieve a list of products.
POST /products - Create a new product.
PUT /products/123 - Update the product with ID 123.
DELETE /products/123 - Delete the product with ID 123.
PATCH /products/123 - Update certain fields of the product with ID 123.


5. What is the difference between PUT and POST?
Answer:

POST is used to create a new resource. It is generally used when the client does not know the exact URI of the resource.
PUT is used to update an existing resource or create a resource if it does not exist. It is idempotent, meaning multiple identical requests should have the same effect as a single request.
Example:

POST /users might create a new user.
PUT /users/123 might update the user with ID 123 or create a new user with ID 123 if it does not exist.


6. What are the common status codes in REST?
Answer: Some common HTTP status codes in REST are:

200 OK: The request was successful.
201 Created: A new resource was successfully created.
204 No Content: The request was successful but there is no representation to return.
400 Bad Request: The request could not be understood or was missing required parameters.
401 Unauthorized: Authentication failed or user does not have permissions for the requested operation.
404 Not Found: The requested resource could not be found.
500 Internal Server Error: An error occurred on the server.


7. How do you handle errors in a RESTful service?
Answer: Errors in RESTful services are typically handled using HTTP status codes and a descriptive error message in the response body.

Example:

json
Copy code
{
  "status": 400,
  "error": "Bad Request",
  "message": "Invalid user ID provided"
}


8. What is idempotency in REST?
Answer: Idempotency means that making multiple identical requests should have the same effect as making a single request. This property is significant for safe operations like GET and PUT.

Example:

PUT /users/123 - Updating the user with ID 123 with the same data multiple times should result in the same state.


9. What is HATEOAS?
Answer: HATEOAS (Hypermedia As The Engine Of Application State) is a constraint of REST that specifies that clients interact with the application entirely through hypermedia provided dynamically by application servers.

Example: A user resource might contain links to related resources:

json
Copy code
{
  "id": 123,
  "name": "John Doe",
  "links": [
    {"rel": "self", "href": "/users/123"},
    {"rel": "orders", "href": "/users/123/orders"}
  ]
}


10. What is content negotiation in REST?
Answer: Content negotiation is a mechanism for serving different representations of a resource at the same URI, based on the client's capabilities or preferences specified in the Accept header.

Example:

GET /users/123 with Accept: application/json might return JSON.
GET /users/123 with Accept: application/xml might return XML.



11. What is a RESTful endpoint?
Answer: A RESTful endpoint is a URL that identifies a resource within the API and the operation to be performed on that resource using HTTP methods.

Example:

GET /books - Retrieve a list of books.
POST /books - Create a new book.



12. What is the purpose of the OPTIONS method in REST?
Answer: The OPTIONS method is used to describe the communication options for the target resource. It allows clients to determine the allowed methods, CORS headers, etc.

Example: OPTIONS /users might return allowed methods like GET, POST, PUT, DELETE.


13. What is a RESTful URI?
Answer: A RESTful URI is a URL that adheres to REST principles, representing resources with clear, hierarchical, and meaningful paths.

Example:

/users/123 - Represents the user with ID 123.
/products/567/reviews - Represents reviews of the product with ID 567.



14. What is versioning in REST and how can it be implemented?
Answer: Versioning in REST is the practice of managing changes to the API without breaking existing clients. It can be implemented in various ways:

URI Versioning: /v1/users
Header Versioning: Accept: application/vnd.myapp.v1+json
Query Parameter Versioning: /users?version=1

Example:

GET /v1/users/123 might return the user in the format of version 1.


15. How can you secure a RESTful API?
Answer: RESTful APIs can be secured using various methods:

Authentication: Using tokens (JWT, OAuth2), API keys, etc.
Authorization: Ensuring that users have permissions to access resources.
HTTPS: Encrypting data in transit.
Rate Limiting: Protecting against DoS attacks.
Example: Using JWT for authentication:

json
Copy code
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}


16. What is a RESTful service's statelessness?
Answer: Statelessness means that each request from a client to a server must contain all the information needed to understand and process the request. The server does not store any state about the client session.

Example: Each GET /users/123 request should be self-contained, providing all necessary authentication and context.


17. What is the difference between REST and SOAP?
Answer:

REST: An architectural style using standard HTTP methods and is stateless. It's generally simpler and uses various formats (JSON, XML).
SOAP: A protocol that follows strict standards, uses XML for messaging, and is generally more complex and heavyweight.
Example: REST endpoint: GET /users/123
SOAP endpoint: <soap:Envelope>...</soap:Envelope>




18. What is the use of the HEAD method in REST?
Answer: The HEAD method is similar to GET, but it does not return the response body. It is used to retrieve the headers for a resource, often to check if it exists or to see metadata.

Example: HEAD /users/123 to check if the user with ID 123 exists.



19. What are query parameters in REST?
Answer: Query parameters are key-value pairs added to the end of a URL to filter or modify the results.

Example: GET /users?role=admin - Retrieves users with the role of admin.


20. What are path parameters in REST?
Answer: Path parameters are variables in the URL path used to identify specific resources.

Example: In /users/{id}, {id} is a path parameter that identifies a specific



URI Components


Scheme: Indicates the protocol (e.g., http, https, ftp, mailto).
Authority: Consists of the domain name or IP address, and optionally includes a port (e.g., example.com, ftp.example.com:21).
Path: The hierarchical path to the resource (e.g., /resource, /docs/page.html).
Query: Provides additional parameters (e.g., ?key=value&otherkey=othervalue).
Fragment: Identifies a specific part of the resource (e.g., #section2).
URL Example Breakdown
plaintext
Copy code


https://www.example.com:8080/docs/tutorial.html?name=networking&chapter=1#introduction
Scheme: https
Authority: www.example.com:8080
Path: /docs/tutorial.html
Query: name=networking&chapter=1
Fragment: #introduction
Conclusion
All URLs are URIs, but not all URIs are URLs.
URIs can be used to identify any resource, while URLs specifically provide the means to locate and access resources over the Internet.


REST, which stands for REpresentational State Transfer, is a set of guidelines for designing web services. It  defines how data should be exchanged between different applications on the web. Here's a breakdown of the key terms:

the client asks for some data of some entity type in some representation, and  server has to respond
here rest gives flexibility 
our client can ask particular representation of data
give me data in csv, xml, json, text
client has an option to ask from the server a particular data in a particular representation which is why it is called as representation state transfer


the idea is any and every request that comes from the client that request has to happen over a resource this resource is typically specified in http url that we send 

anything that we want to do we can specify as verb, this is the action that I want to take and this is the resource on which I want to to take this action

Rest says you can choose any proototcol like http or tcp, rest is just a specifictaion 


Rest goes well with http 
Http verbs -->  GET, PUT, POST, DELETE has well defined meaning so by seeing a particular verb we could anticipate its purpose

delete /users/1  --> delete the resource of type user identified by 1
http verbs are multiplex

e.g --> get a student details  GET /student/1 -> instead of endpoint like /getstudent 
update a student details POST /student/1  --> instead of having endpoint like /updatastudent
noone enforcing us to do it this way that is the rest way of doing it

I could have expose enddpoint /getstudent and passing id in body and getting this information that is also an http endpoint but this is not REST implementation that is the difference

REST says use HTTP method wisely the url should be an identification of your resource and not the action you are taking 

Representational: Information on the web is represented in resources. These resources can be anything from a document to an image or even an entire database. They are identified by URIs (Uniform Resource Identifiers), which are essentially web addresses.
State: In REST, the server doesn't need to remember anything about the client's past interactions (like a shopping cart on a website). Each request from the client is treated independently. This makes RESTful systems simpler and more scalable.
Transfer: Data is transferred between client and server using standard HTTP methods. These methods act like verbs telling the server what to do with the resource. Common methods include:
GET: Retrieves information from a resource. (Imagine browsing a product page)
POST: Creates a new resource. (Think submitting a form)
PUT: Updates an existing resource. (Like editing a profile)
DELETE: Removes a resource. (Deleting an item from your cart)
By following these principles, REST promotes a standardized way for applications to communicate and exchange data efficiently on the web.'''
'''


SOAP:

Uses XML for messaging.
Strict, standard protocol.
Supports complex operations.
More overhead due to extensive XML parsing.
REST:

Uses standard HTTP methods.
Resources identified by URLs.
Can return various data formats (e.g., JSON, XML).
Stateless and simpler than SOAP.

GraphQL:

Clients specify exactly what data they need.
Single endpoint for all requests.
Reduces over-fetching and under-fetching of data.
Requires a defined schema and resolvers on the server.


SOAP (Simple Object Access Protocol)
SOAP is a protocol used for exchanging structured information in the implementation of web services. It's designed to be platform and language-independent, relying on XML (Extensible Markup Language) to format messages.

Key Concepts:
XML-Based Messaging:

SOAP messages are encoded in XML.
They are made up of an envelope, a header (optional), and a body.
Envelope:

The root element of a SOAP message.
Defines the start and end of the message.
Header:

An optional part that can contain metadata such as authentication data, transaction management, etc.
Body:

Contains the actual message intended for the recipient.
Can include one or more child elements that define the operation being requested and any parameters.
How SOAP Works:
Client Requests:

The client application generates a SOAP request message in XML format.
This message specifies the desired operation and any necessary parameters.
Sending the Request:

The client sends the SOAP message over a network protocol, typically HTTP or HTTPS.
Server Processing:

The server receives the SOAP message.
It parses the XML to understand the requested operation and parameters.
The server processes the request, performs the operation, and generates a response message in XML.
Client Receives Response:

The server sends back the SOAP response message.
The client receives this message, parses the XML, and extracts the results.
Example:
A SOAP request to get a user's information might look like this:'''



<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:example">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetUserInfo>
         <urn:UserID>12345</urn:UserID>
      </urn:GetUserInfo>
   </soapenv:Body>
</soapenv:Envelope>


The server's response might look like this:



<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:example">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:GetUserInfoResponse>
         <urn:UserName>John Doe</urn:UserName>
         <urn:Email>john.doe@example.com</urn:Email>
      </urn:GetUserInfoResponse>
   </soapenv:Body>
</soapenv:Envelope>



