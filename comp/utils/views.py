from django.shortcuts import redirect
from django.contrib.auth.views import login as django_login

def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return redirect('/')
    kwargs['template_name'] = 'login.html'
    return django_login(request, *args, **kwargs)
