from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from users_manager.core import views as user_views
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.
def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)
    