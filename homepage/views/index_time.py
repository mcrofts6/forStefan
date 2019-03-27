from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
import random

@view_function
def process_request(request):
    context = {
        'now': datetime.now(),
    }
    return request.dmp.render('index_time.html', context)