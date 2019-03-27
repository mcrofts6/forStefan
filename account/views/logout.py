from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect
from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from account import models as amod
from account.views.login_form import LoginForm


@view_function
def process_request(request):
        logout(request)

        return HttpResponseRedirect('/account/login')


