## 3.2 Creating App
### Creating Models
Models are just classes for each database field that are located in `models.py` in the app directory. In this case `bookings/` for the bookings app

Once classes are created for each field, add the app to the `INSTALLED_APPS` setting within `movie_theater_booking`

Next, run 
```bash 
python manage.py makemigrations [app_name]
```

Finally, run
```bash
python manage.py migrate
```

>[!note] Model Change 3-Step Guide
>- Change models in `models.py`
>- Run `python manage.py makemigrations [app_name]` to create migrations for the model changes
>- Run `python manage.py migrate` to apply changes to the database

### Creating Admin User

## 3.3  Creating the MVT Architecture
### Model
Model portion covered in [[#3.2 Creating App]]

### View
Right now I am stuck trying to figure out how to how to implement the Model View Template (MVT) structure. I created a serializer file like in the tutorial, but I'm not sure what this file does or if its necessary for what 3.3 is asking me to do.

From my understanding the serializer jsonifys database entries and serves them to give APIs access to the database?

I am still trying to figure out how to do this part of the assignment. I am using this [Serializers - Django REST framework](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer) part of the DRF docs to see how to map serializers to my Models and what that relationship looks like.

I ended up implementing the serializers with the bare minimum given in the docs: [Serializers - Django REST framework](https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include).

----

Now, creating the views is confusing me as well. From what I currently understand, the DRF ModelViewSet [Viewsets - Django REST framework](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset) automatically implements the CRUD operations for a RESTful application. The actions provided by the `ModelViewSet` class are `.list()`, `.retrieve()`, `.create()`, `.update()`, `.partial_update()`, and `.destroy()`. You can override any of these to implement your own behavior or the function. 

I don't know if what I have is good enough to proceed or if there is more complexity that I need to put into this `views.py` file. 

---
### Template

## 3.4 Creating an Attractive User Interface
I'm just going to use plain Bootstrap to get everything going at a bare minimum for POC.

## Super user sign-in credentials 
USERNAME: admin
PASSWORD: admin