# API

**(Application Programming Interface)** : is an interface that allows software applications to communicate with each other.

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