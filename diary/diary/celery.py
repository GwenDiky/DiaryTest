from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diary.settings')

app = Celery('diary',
             broker='amqp://guest@localhost//',
             include=['diary'] #References your tasks. Donc forget to put the whole absolute path.
             )

app.conf.update(
        CELERY_TASK_SERIALIZER = 'json',
        CELERY_RESULT_SERIALIZER = 'json',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_TIMEZONE = 'Europe/Moscow',
        CELERY_ENABLE_UTC = True
                )
