from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from django.contrib.auth import authenticate, login
from account.views.login_form import LoginForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


@view_function
def process_request(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        context = {
        'form': form,
        }
        if form.is_valid():
            
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            # A backend authenticated the credentials
            login(request, user)
            return HttpResponseRedirect('/homepage')
            # No backend authenticated the credentials
        else:
            context = {
                'form': form,
            }
    else:
        form = LoginForm()
        context = {
            'form' : form,
        }
    
    return request.dmp.render('login.html', context)



