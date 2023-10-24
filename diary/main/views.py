from django.views.generic.edit import FormView
from django.views.generic.edit import FormView
from django.http import HttpResponse, JsonResponse
from .forms import MessageForm
import json
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from diary.tasks import clear_queue

class MessageView(FormView):
    template_name = 'main/message.html'
    form_class = MessageForm

    def form_valid(self, form):
        form.create_json()
        msg = 'Your message has been posted.'
        return redirect('message')

    
def json_to_html(request):
    with open(f'{settings.STATICFILES_DIRS[0]}\sample.json') as f:
        templates = json.load(f)
    
    return render(request, 'main/message_list.html', templates)

def clear_queue_view(request):
    try:
        # вызов задачи Celery для очистки очереди
        result = clear_queue.apply_async()
        return JsonResponse({'status': 'Task enqueued', 'task_id': result.id})
    except Exception as e:
        return JsonResponse({'status': 'Error', 'error': str(e)}, status=500)
