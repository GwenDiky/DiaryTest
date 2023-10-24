# DiaryTest2
Django + Celery + RabiitMQ

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

celery -A mysite worker -l info

_Make sure you have RabbitMQ service running._

rabbitmq-server
