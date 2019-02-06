from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime

@view_function
def process_request(request):
    context = {}
    # did a form get submitted, or is this first visit to the page?
    if request.method == "POST":
        print('name: ' + request.POST['yourname'])
        print('email: ' + request.POST['youremail'])
        print('happy: ' + request.POST['happy'])
        return HttpResponseRedirect('/homepage/index')
        #if no:
            #mark the error
        #continue with or without form
    else:
        return request.dmp.render('contact.html', context)

