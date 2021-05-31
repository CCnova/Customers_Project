Before jumping to the API you need Django installed, you can follow the instructions here: https://docs.djangoproject.com/en/3.2/intro/install/ <br /> <br />

You can setup the project running one single command, open a terminal and type: <br /> <br />
    `python manage.py setup_project` <br /> <br />

In case the above fail, you can follow the instructions below.

To run the application you need to install some packages first, please open a terminal and run this commands: <br /> <br />
(1)    `pip install django-extensions` <br />
(2)    `pip install python-dotenv` <br />
(3)    `pip install djangorestframework` <br /><br />
1 - Necessary for running the customer database seeder script <br />
2 - Necessary for configuring the environment variables <br />
3 - Necessary for http funcionalities <br /><br />

Now execute the migrations to create the database structure: <br />
    `python manage.py migrate` <br /> <br />

After installing the dependencies, you can populate the database with a django management command <br />

Running the populate command: <br /> <br />
  Open a terminal and run the command: <br />

    python manage.py load_customers
  
  This will make the application load data from the customers csv file located in customers/data <br /><br />

You need an google maps API Key to populate the customer geo-location. <br />
You can search for instructions about how to get
an API KEY here: https://developers.google.com/maps/documentation/geolocation/overview <br /> <br />
After getting an API KEY, you need to create an .env file to populate with the key. Just copy the .env.example, rename
to .env and Past you api key on the GOOGLE_MAPS_API_KEY field. <br /> <br />


After you setup the project you can head to http://127.0.0.1:8000/api and start consuming the API from a simple webpage <br />