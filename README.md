# Reto11_BookstoreAPI

## Introduction
This proyect is a task for a Django Backend Bootcamp at [Geekshubs Accademy](https://geekshubsacademy.com). 
It is a REST API built with Django Rest Framework. 
In this API the user can create, read, update or delete objects representing two linked models: _Author_ and their _Book(s)_.
This API uses a PostgreSQL database.

## Author
Sole author of this project: Valentin Piombo - valenp97@gmail.com - www.github.com/veziop

## Using the API
First, position the terminal at the root directory (containing 'api_bookstore/' - 'Biblioteca/' - 'manage.py' ) and run the server with: <br><br>
```python manage.py runserver```

<br>Then open your browser at "[http://127.0.0.1:8000/author/](http://127.0.0.1:8000/author/)" to see the current list of authors. 
This list is very brief, add more by filling the form at the bottom of the page and click **POST**.

To update, partially update or delete an entry go to its endpoint 'hero/_pk_' where pk is it's ID and click on **DELETE**. Alternatively click on 
Raw Data to edit the JSON input and finally click **PUT** to update, or **PATCH** to partially update.

<br>
To operate the Book objects go to [http://127.0.0.1:8000/book/](http://127.0.0.1:8000/book/) and treat it
the same manner as with /author/.


<br>
<br>

------------------------------
<br>

## Models
The first model in this project is Author, and it has four attributes:
* id - Big Int Primary Key
* name - Charfield (the name of the superhero eg: Carl, Rupert)
* created_date - DateFrield (the date of the creation of the instance into the database)
* added_by_id - ForeignKey (the id of the User that created the instance)

<br>

The second model is Book, and it holds a One-to-Many relationship with the model Author. Its six attributes:
* id - Big Int Primary Key
* title - CharField (the title of the book)
* description - CharField (the description of the book)
* author - ForeignKey (the id of the Author model of the book)
* created_date - DateField (the date of the creation of the instance into the database)
* added_by_id - ForeignKey (the id of the User that created the instance)


## Serializers
There are two serializer: _BookSerializer_ and _AuthorSerializer_. Both are set up to be in charge of serializing their respective model's data.

## Viewsets
As with the serializers, there are two  ViewSet to manage all CRUD operations. These viewsets are called _BookViewSet_ and _AuthorViewSet_, they inherit from ModelViewSet.

## URLConfig
One router is used to register two endpoints: 'author/' and 'book/'. The parent ModelViewSet helps with the default routes 'author/<<int:pk>>/' and 'book/<<int:pk>>/'for operations regarding
one specific object.

## Moving forward
This project is very rudimentary, so next projects should include very important REST components like permissions, JWT, tests, authentication, etc. 
