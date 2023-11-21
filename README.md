# cs361-ms-username
CS361 Microservice application to generate random usernames

## Description
This microservice accepts an email address and returns three random username options based on the email address.

## Calling the Service
The service is called using an HTTP POST request to: https://mellit-cs361.wl.r.appspot.com/username_generator
The request must include a body in JSON forrmat.

### Example request body

```
{
  "email": "example@email.com",
  "source": "sourceID"
}
```
* **email**: the email of the user (required)
* **source**: ID of the source/target element to update upon HTTP response (optional)

### Example programmatic request in Python
```
import requests

url = 'https://mellit-cs361.wl.r.appspot.com/username_generator'
req_body = {'email': 'example@email.com', 'source':'sourceID'}

response = requests.post(url, json = req_body)
```


## Service Response
Upon successful call to the service, an HTTP response will be sent back with a JSON-format body.

### Example response body
```
{
  "usernames": ["example094756", "examplePlantsTrees", "exampleA8x93gh"],
  "source": "sourceID"
}
```
* **usernames**: list of potential usernames to display to the user
* **source**: ID of the source/target element to update upon HTTP response (optional)

### Example programmatic receipt in Python
```
response_body = response.json()

target = response_body['source']
values = response_body['usernames']
```

## UML Diagram
![username_uml](https://github.com/tessa-melli/cs361-ms-username/assets/72112957/f1e97d05-ce8a-46a6-89e7-7b98af8f5b22)

