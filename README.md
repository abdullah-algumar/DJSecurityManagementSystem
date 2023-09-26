# Small Scale Security Management System

### This Project:

- Register security guard (name, surname, date of birth, years of experience)
- Assign Duty Time (for example, Morning 9 am to 6 pm, override control should be done)
- List page of security guards registers when clicked duty time should be shown.

# How to Install

### Create a virtual environment:

`python3 -m venv env`

### Activate the virtual environment:

`source env/bin/activate`

### Install requirements:

`pip3 install -r requirements.txt`

### Create a environment file in the BASE_DIR named .env and put the informations:

```
touch .env
```

```
DEBUG=True
SECRET_KEY=<secret-key>
POSTGRES_DB=<db-name>
POSTGRES_USER=<db-user>
POSTGRES_PASSWORD=<db-password>
DATABASE_HOST=<db-host>
DATABASE_PORT=5432
```

### Make migrations for database tables creating:

`python3 manage.py makemigrations`

### Migrate:

`python3 manage.py migrate`

### Create a superuser for app management:

`python3 manage.py createsuperuser`

## Run the server:

`python3 manage.py runserver`

# Create the dummy data for models using command

`python3 manage.py populate_data`

# RUN with Docker

`docker-compose up`
