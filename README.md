env

# TANGENT SOLUTIONS TEST

author Reagan Scofield


# REQUIREMENTS

1. Linux Ubuntu Server
2. PostgreSQL Server

clone repository

```
   $ git clone https://github.com/reaganscofield/tangent_solutions.git

   $ cd tangent_solutions
```

# SETUP VIRTUAL ENVIRONMENT

```
    $ sudo apt install virtualenv
    $ virtualenv -p python3 virtual_env
    $ source virtual_env/bin/activate
```

# INSTALL LIBRARIES

```
    $ pip install -r requirements.txt
```

if you run into the problem please install libraries one by one

```
    $ pip install Django
    $ pip install djangorestframework
    $ pip install psycopg2
```

# SETUP DATABASE

login to your PostgreSQL Server and create database "tangent_solutions"
in case you are not using the default username and password please make sure
you have updated your DB_USERNAME with your database username DB_PASSWORD
with your database password

create env.py file and open it with vim 

```
    $ cd tagent_project
    $ touch env.py
    $ vim env.py
```

add this code and save it

```
    DB_ENGINE = 'django.db.backends.postgresql'
    DB_NAME = 'tangent_solutions'
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_HOST = 'localhost'
    DB_PORT = ''`
```

# MIGRATE DATABASE & RUNNING PROJECT

please make sure that you virtual_env still activated

```
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```

# TESTING API

view list of EMPLOYEE in JSON FORMAT and create EMPLOYEE

```
    http://127.0.0.1:8000/api/employeers/
```

view single EMPLOYEE JSON FORMAT according to given primary key in the url '/1/' it will query EMPLOYEE with PK 1

```
    http://127.0.0.1:8000/api/employeers/1/
```

view list of LEAVES in JSON FORMAT and create LEAVE

```
    http://127.0.0.1:8000/api/leaves/
```

view single LEAVE in JSON FORMAT according to given primary key in the url '/1/' it will query LEAVE with PK 1

```
    http://127.0.0.1:8000/api/leaves/1/
```


# RUNNING UNIT TESTS

```
    $ python manage.py test
```
