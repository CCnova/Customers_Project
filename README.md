
To run the application you need to install some packages first, please open a terminal and run this commands: <br />
(1)    pip install django-extensions <br />
(2)    pip install python-dotenv <br />
1 - Necessary for running the customer database seeder script <br />
2 - Necessary for configuring the environment variables <br />

After installing the dependencies, you have two options: Populate the database with a pre-made script or enter the admin environment and populate by hand <br />

1 - Running the populate script: <br /> <br />
  Open a terminal and run the command: <br />

    python manage.py runscript load_customers
  
  This will make the application load data from the customers csv file located in customers/data <br />

2 - Enter Django admin environment: <br />
    Go to http://127.0.0.1:8000/admin and enter this admin credentials <br /> <br />
      username: owlish <br />
      email: owlish@email.com <br />
      password: owlselection123 <br />
    
After you populated the database you can head to http://127.0.0.1:8000/ and start consuming the API from a simple webpage <br />