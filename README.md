Before jumping to the API you need Django installed, you can follow the instructions here: https://docs.djangoproject.com/en/3.2/intro/install/ <br /> <br />

To run the application you need to install some packages first, please open a terminal and run this commands: <br />
(1)    pip install django-extensions <br />
(2)    pip install python-dotenv <br />
(3)    pip install djangorestframework <br />
1 - Necessary for running the customer database seeder script <br />
2 - Necessary for configuring the environment variables <br />
3 - Necessary for http funcionalities <br /><br />

Now execute the migrations to create the database structure: <br />
    python manage.py migrate <br /> <br />

After installing the dependencies, you can populate the database with a django management command <br />

Running the populate command: <br /> <br />
  Open a terminal and run the command: <br />

    python manage.py load_customers
  
  This will make the application load data from the customers csv file located in customers/data <br />
    
After you populated the database you can head to http://127.0.0.1:8000/api and start consuming the API from a simple webpage <br />