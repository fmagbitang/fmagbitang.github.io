# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django (2.1)
- Django REST Framework
- Django Rest Auth

## Installation
```
	pip install django
	pip install djangorestframework
	pip install django-rest-auth
	pip install django-allauth
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `shapes`, so we will use the following URLS - `/rectangle or square or triangle/`, `/rectangle or square or triangle/<id>/perimeter/`, `/rectangle or square or triangle/<id>/area/`, for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`rectangle` | GET | READ | Get all rectangle shape
`square` | GET | READ | Get all square shape
`triangle` | GET | READ | Get all triangle shape
`rectangle/:id/perimeter` | GET | READ | Get a single rectangle shape
`rectangle/:id/area` | GET | READ | Get a single rectangle shape
`square/:id/perimeter` | GET | READ | Get a single square shape
`square/:id/area` | GET | READ | Get a single square shape
`triangle/:id/perimeter` | GET | READ | Get a single triangle shape
`triangle/:id/area` | GET | READ | Get a single triangle shape
`rectangle`| POST | CREATE | Create a new rectangle shape
`square`| POST | CREATE | Create a new square shape
`triangle`| POST | CREATE | Create a new triangle shape
`rectangle/:id` | PUT | UPDATE | Update a rectangle shape
`square/:id` | PUT | UPDATE | Update a square shape
`triangle/:id` | PUT | UPDATE | Update a triangle shape
`rectangle/:id` | DELETE | DELETE | Delete a rectangle shape
`square/:id` | DELETE | DELETE | Delete a square shape
`triangle/:id` | DELETE | DELETE | Delete a triangle shape

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
	python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
	http  http://127.0.0.1:8000/triangle/3/area
```
we get:
```
 {  "detail":  "You must be authenticated"  }
```
Instead, if we try to access with credentials:
```
	http http://127.0.0.1:8000/triangle/3/area "Authorization: Token 7530ec9186a31a5b3dd8d03d84e34f80941391e3"
```
we get the shape with id = 3
```
{
    "id": 3,
    "length1": "5",
    "length2": "6",
    "length3": "7",
    "area": "14.696938456699069",
    "perimeter": "18",
    "created_at": "2019-04-26T01:59:36.815177+08:00",
    "updated_at": "2019-04-26T01:59:36.815221+08:00"
}
```

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="12345789"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

The API has some restrictions:
-   The shapes are always associated with a creator (user who created it).
-   Only authenticated users may create and see shapes.
-   Only the creator of a shape may update or delete it.
-   Unauthenticated requests shouldn't have access.

### Commands
```
http http://127.0.0.1:8000/rectangle/ "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/square/ "Authorization: Token <YOUR_TOKEN>"
http http://127.0.0.1:8000/triangle/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/rectangle/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/square/ "Authorization: Token <YOUR_TOKEN>"
http GET http://127.0.0.1:8000/triangle/ "Authorization: Token <YOUR_TOKEN>"
http POST http://127.0.0.1:8000/rectangle/ "Authorization: Token <YOUR_TOKEN>" width="5" height="6"
http POST http://127.0.0.1:8000/square/ "Authorization: Token <YOUR_TOKEN>" side="4"
http POST http://127.0.0.1:8000/triangle/ "Authorization: Token <YOUR_TOKEN>" length1="5" length2="6" length3="7"
http PUT http://127.0.0.1:8000/rectangle/3 "Authorization: Token <YOUR_TOKEN>" width="7" height="8"
http PUT http://127.0.0.1:8000/square/3 "Authorization: Token <YOUR_TOKEN>" side="8"
http PUT http://127.0.0.1:8000/triangle/3 "Authorization: Token <YOUR_TOKEN>" length1="8" length2="9" length3="10"
http DELETE http://127.0.0.1:8000/rectangle/3 "Authorization: Token <YOUR_TOKEN>"
http DELETE http://127.0.0.1:8000/square/3 "Authorization: Token <YOUR_TOKEN>"
http DELETE http://127.0.0.1:8000/triangle/3 "Authorization: Token <YOUR_TOKEN>"
```