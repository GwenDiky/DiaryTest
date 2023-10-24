from django.urls import path
from main.views import MessageView, json_to_html, clear_queue

urlpatterns = [
    path('', MessageView.as_view(), name='main'),
    path('message', json_to_html, name='message'),
    path('message/clear', clear_queue, name='clear-queue'),
]