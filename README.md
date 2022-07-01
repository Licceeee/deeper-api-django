# deeper-api-django
card game backend

## Project Set up

### Clone
`git clone https://github.com/Licceeee/deeper-api-django.git`

### virtualenv
`cd deeper-api-django`

`virtualenv -p python3 venv`

`source venv/bin/activate`

### install dependencies
`poetry install`

### migrate
`cd deeper`

`python manage.py makemigrations`

`python manage.py makemigrations card`

`python manage.py migrate`

### create superuser
`python manage.py createsuperuser`



<!-- ### TODO setup postgres
`psycopg2-binary`

`
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': '[dbname]',
    'USER': '[dbadmin]',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '',
}
` -->
