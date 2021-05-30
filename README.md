
To run the application you need to install some packages first, please open a terminal and run this commands:
(1)    pip install django-extensions
(2)    pip install python-dotenv
1 - Necessary for running the customer database seeder script
2 - Necessary for configuring the environment variables

After installing the dependencies, you have two options: 1 - Populate the database with a pre-made script, 2 - Enter the admin environment and populate by hand

1 - Running the populate script:
  Open a terminal and run the command:

    python manage.py runscript load_customers
  
  This will make the application load data from the customers csv file located in customers/data

2 - Enter Django admin environment:
    Go to http://127.0.0.1:8000/admin and enter this admin credentials
      username: owlish
      email: owlish@email.com
      password: owlselection123
    
After you populated the database you can head to http://127.0.0.1:8000/ and start consuming the API from a simple webpage