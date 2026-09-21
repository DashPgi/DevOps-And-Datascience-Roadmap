# API

**(Application Programming Interface)** : is an interface that allows software applications to communicate with each other.

### Client
The system that sends the request.

Examples:
```
- Browser
|
- Mobile app
|
- Python application
```
### Host
The server/address where the service is running.

Example:
```
api.example.com
```

### Endpoint
A specific URL/path used to access a resource or API function.

Example:
```
GET https://api.example.com/users
```

# Type of API
**APIs can be categorized in different ways** :
### By architecture
1. **REST API** : Common, uses HTTP and usually JSON.
2. **SOAP API** : XML-based and highly standardized.
3. **GraphQL API** : Clients request exactly the data they need.
4. **gRPC API** : Fast, commonly used for microservices.
5. **WebSocket API** : Provides real-time, two-way communication.
### By accessibility
1. **Public API** : Available to external developers.
2. **Private API** : Used internally within an organization.
3. **Partner API** : Available to specific business partners.

---
# HTTP Method
An HTTP Method specifies what action the client wants the server to perform.
### GET and POST
GET and POST are two HTTP methods commonly used with APIs.

| Method      | Purpose                               |
| ----------- | ------------------------------------- |
| **GET**     | Retrieve data                         |
| **POST**    | Create / submit new data              |
| **PUT**     | Replace a resource completely         |
| **PATCH**   | Partially update a resource           |
| **DELETE**  | Delete a resource                     |
| **HEAD**    | Get headers without the response body |
| **OPTIONS** | Check allowed methods/capabilities    |
| **CONNECT** | Establish a network tunnel            |
| **TRACE**   | Diagnostic request tracing            |

```
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

**Main difference: GET usually sends parameters through the URL, while POST usually sends data in the request body.**

## .venv
**.venv is commonly a Python Virtual Environment.**

## curl
**curl is a command-line tool for sending requests and receiving responses, commonly over HTTP.**
## Json
**JSON (JavaScript Object Notation) is a text-based format for storing and exchanging data, widely used in APIs.**
```
{
    "name" : "be to che",
    "age" : 00,
    "store" : "pgstore"
}
```

# Flask
**Flask is a lightweight Python web framework used to build web applications and APIs.**

Flask = A Python framework for building web servers and APIs.

Example : 
```
from flask import Flask

app = Flask(__name__)

@app.get("/users")
def users():
    return {"name": "Ali", "age": 20}
```
# FastAPI
FastAPI is a modern Python web framework mainly designed for building APIs.It provides:

- High performance
- REST API support
- Data validation with Pydantic
- Automatic API documentation
- async/await support

# JWT

### User Authentication
- Cookie-based Authentication
- Token-based Authentication
    ```
    Request : 
        web.app ---- {Passwrd,usrname} ---> Server/API
    Response : 
        web.app <--- {Token} ---- Server/API
    Repeat : 
        web.app <--- {Token} ---> Server/API
    ```
- Session-based Authentication
    ```
    Request : 
    Client ---- {Passwrd,usrname} ---> Server
    Response : 
    Client <--- {Authentication} ---- Server
    Repeat :
    Client ---- {Passwrd,usrname} ---> Server
    Client <--- {Authentication} ---- Server
    ```