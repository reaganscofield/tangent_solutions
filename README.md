env

$ sudo apt install virtualenv

$ virtualenv -p python3 virtual_env

$ source virtual_env/bin/activate




# DATABASE SETUP 



$ cd tagent_project

$ touch env.py

copy the following code inside your env.py file

```
    DB_ENGINE = 'django.db.backends.postgresql'
    DB_NAME = 'tangent_solutions'
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_HOST = 'localhost'
    DB_PORT = ''`
```