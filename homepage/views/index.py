from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod

@view_function
def process_request(request):


    context = {
        jscontext('now'): datetime.now(),
    }
    return request.dmp.render('index.html', context)

