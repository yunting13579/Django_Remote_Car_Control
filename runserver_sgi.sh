gunicorn -w4 -b "0.0.0.0:8000" --env DJANGO_SETTINGS_MODULE=mysite.settings mysite.wsgi
