web: daphne django_socialmedia.asgi:application --port $port --bind 0.0.0.0
worker: python manage.py runworker channels --settings=django_socialmedia.settings -v2