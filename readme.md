# Features

- [x] View all items in the inventory
- [x] Add items to inventory
- [x] Search the inventory with item names or description
- [x] Edit item price and/or quantity

# Installation

1- Download Docker 
- [docker](https://www.docker.com/products/docker-desktop/)

2- Create the database
```bash
docker run --name=postgres -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgrespw -e POSTGRES_DBNAME=postgres -p 32769:32769 postgres:latest
```
OR if you want to use SQLite <br>
uncomment
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
and comment
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgrespw',
        'HOST': 'localhost',
        'PORT': '32769'
    }
}
```
in the [settings.py](/Small-Inventory-Webapp/SmallInventoryWebapp/settings.py) folder

3- Create a virtual environment and activate it 
```bash
python -m venv env
env\Scripts\activate
```

4- Install the requirements

```bash
pip install -r requirements.txt
```

5- Run these commands
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6- Finally run the server
```bash
python manage.py runserver
```