# movies_REST_API

movies_REST_API is an application written during the programming bootcamp course. The aim of the workshop was to write a backend for the REST application. Main functionality of the application is to handle list of movies.

## Stack

* Python
* MySQL
* REST
* Django REST framework

## How to build the project locally

### 1. Download

You need the movies_REST_API project files in your workspace:

`$ git clone https://github.com/dominikazdybek/movies_REST_API.git`

### 2. Virualenv

Create virtualenv for your project and activate it:

`$ virtualenv -p python3 movies_env`

`$ source movies_env/bin/activate`

### 3. Requirements

Download and install MySQL database (prefered version is 5.7). You can get it from here: 

* https://dev.mysql.com/downloads

To install all required dependencies, simply type:

`$ cd movies_REST_API`

`$ pip install -r requirements.txt`

### 4. How to run?

First, create database called `movies` in MySQL. Then define your credentials in settings file: `django_REST/settings.py`.

Make migration:

* `/manage.py migrate`

Run server:

* `/manage.py runserver`


# REST API Documentation

## Movies

### URL

`/movies` 

### Method

GET | POST


### Data params

```
    {
        "title": [string],
        "description": [string],
        "director_name": [string],
        "actors_list": [string],
        "year": [integer],
    }
```

### Success Response

* **GET**
  * **Code:** 200 <br />
  * **Content:**
 
```
[
    {
        "title": "Zielona Mila",
        "description": "Emerytowany strażnik więzienny opowiada przyjaciółce o niezwykłym mężczyźnie, którego skazano na śmierć za zabójstwo dwóch 9-letnich dziewczynek.",
        "director_name": "Frank Darabont",
        "actors_list": "Tom Hanks, David Morse",
        "year": 1999,
    },
...
]
```

* **POST**
  * **Code:** HTTP_201_CREATED <br />
  * **Content:**  
```
    {
        "title": "Skazani na Shawshank",
        "description": "Adaptacja opowiadania Stephena Kinga. Niesłusznie skazany na dożywocie bankier, stara się przetrwać w brutalnym, więziennym świecie.",
        "director_name": "Frank Darabont",
        "actors_list": "",
        "year": 1994
    }
```

### Error Response

* **POST**
  * **Code:** HTTP_400_BAD_REQUEST <br />
  * **Content:** {error: 'Wrong JSON'}


## MOVIE

### URL

`/movie/:id`

### Method

`GET | DELETE | PUT`

### URL Params

`id=[integer]`

### Success Response:

* **GET**
  * **Code:** 200 <br />
  * **Content:**
```
    {
        "title": "Skazani na Shawshank",
        "description": "Adaptacja opowiadania Stephena Kinga. Niesłusznie skazany na dożywocie bankier, stara się przetrwać w brutalnym, więziennym świecie.",
        "director_name": "Frank Darabont",
        "actors_list": "",
        "year": 1994
    }
```

* **DELETE**
  * **Code:** HTTP_204_NO_CONTENT <br />
  * **Content:** ` `

* **PUT**
  * **Code:** 200 <br />
  * **Content:**
``` 
   {
        "title": "Skazani na Shawshank",
        "description": "Adaptacja opowiadania Stephena Kinga. Niesłusznie skazany na dożywocie bankier, stara się przetrwać w brutalnym, więziennym świecie.",
        "director_name": "Frank Darabont",
        "actors_list": "",
        "year": 1995
    }
```

### Error Response:

* **GET**
  * **Code:** 404 <br />
  * **Content:** {error: 'DoesNotExist'}

* **PUT**
  * **Code:** HTTP_400_BAD_REQUEST <br />
  * **Content:** {error: 'Wrong JSON'}


## PEOPLE

### URL

`/people` 

### Method

GET | POST


### Data params
```
    {
        "id": [integer],
        "name": [string]
    },
```
### Success Response

* **GET**
  * **Code:** 200 <br />
  * **Content:**
 
```
[
    {
        "id": 1,
        "name": "Frank Darabont"
    },
...
]
```

* **POST**
  * **Code:** HTTP_201_CREATED <br />
  * **Content:**  
```
   {
        "id": 2,
        "name": "Tom Hanks"   
    },
```

### Error Response

* **POST**
  * **Code:** HTTP_400_BAD_REQUEST <br />
  * **Content:** {error: 'Wrong JSON'}


## PERSON

### URL

`/person/:id`

### Method

`GET | DELETE | PUT`

### URL Params

`id=[integer]`

### Success Response:

* **GET**
  * **Code:** 200 <br />
  * **Content:**
```
    {
        "id": 1,
        "name": "Frank Darabont"
    },
```

* **DELETE**
  * **Code:** HTTP_204_NO_CONTENT <br />
  * **Content:** ` `

* **PUT**
  * **Code:** 200 <br />
  * **Content:**
``` 
  {
        "id": 1,
        "name": "Frank Darabon" 
  },

```

### Error Response:

* **GET**
  * **Code:** 404 <br />
  * **Content:** {error: 'DoesNotExist'}

* **PUT**
  * **Code:** HTTP_400_BAD_REQUEST <br />
  * **Content:** {error: 'Wrong JSON'}
