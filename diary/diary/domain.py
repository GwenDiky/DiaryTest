import time
import os
import json
from django.conf import settings

def real_job_doer(name,message):
    context = {
        'username': name,
        'msg': message
    }
    json_object = json.dumps(context, indent=4)
    time.sleep(5)
    path = os.path.join(settings.STATICFILES_DIRS[0],"sample.json")
    with open(path, 'w') as f:
        f.write(json_object)