# deeper-django
card game backend

## Project Set up

### Clone
`git clone https://github.com/Licceeee/deeper-django.git`

### virtualenv
`cd deeper-django`

`virtualenv -p python3 venv`

`source venv/bin/activate`

### install dependencies
`poetry install`

### migrate
`cd deeper`

`python manage.py makemigrations`

`python manage.py migrate`

### create superuser
`python manage.py createsuperuser`

### install graphene 
`poetry add graphene-django`

### add to installed apps in settings.py
`INSTALLED_APPS = [
    "django.contrib.staticfiles", # Required for GraphiQL
    "graphene_django", ]`

### add url in root urls.py
`from django.urls import path`
`from graphene_django.views import GraphQLView`

`urlpatterns = [
    # ...
    path("graphql", GraphQLView.as_view(graphiql=True)),
]`

### define the schema location for Graphene in the settings.py 
`GRAPHENE = {
    "SCHEMA": "django_root.schema.schema"
}`




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
