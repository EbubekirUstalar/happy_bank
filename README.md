# Scenario

HappyBank is the most customer friendly and secure banking provider in the world.
To make sure nothing goes wrong, we need your help

# How to get this up and running

## Initial Project setup
    git clone 'project_path'
    python -m venv happy_bank_venv
    source happy_bank_venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver

After running the server you should be able to see wellcome page on [http://127.0.0.1:8000](http://127.0.0.1:8000/)
The app will bind to port 8000 so please make sure the port is not already in use. Stop all other containers to be sure.

Once everything is built and running, you should migrate your database by running ```python manage.py migrate```.


To get into the Django shell, use ```python manage.py shell```.
Run ```python manage.py test``` to execute the tests.

# What we prepared for you

The project consists of three models ```BankAccount```, ```BankAccountOwner``` and ```Transaction```.
When a transfer is made from one bank account to another, two transactions are created: a negative one for the sending account and a positive one for the receiving account. See ```BankAccount.transfer```.

You can use the management command ```initialize_data``` to seed the database with some test data. Run ```python manage.py initialize_data``` to execute it.

In order to see the initialized data you can create a superuser and visit; http://127.0.0.1:8000/admin/
```python manage.py createsuperuser```


There are already some tests implemented and some scaffolds for more tests.

# Tasks

You have 24 hours before the interview.

Use this time to get the project running and get familiar with it.

The tasks will be shared with you when you start sharing your screen.

After you are done with the tasks, please create a branch and a pull request.

If you have problems please reach out to us.
