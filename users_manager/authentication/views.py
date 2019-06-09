from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from users_manager.core import views as user_views
from django.contrib.auth.models import User, Group
from .models import UserProfile
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    next = ''
    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,
                  user,
                  backend='user_managers.backends.EmailAuthenticationBackend')

            if next == '':
                return HttpResponseRedirect('/users')
            else:
                return HttpResponseRedirect(next)
        else:
            response = {}
            response['login_error_invalid'] = 'Incorrect username or password'
            response['next'] = next

            return render(request, "login.html", response)
    else:
        return render(request, "login.html", {'next': next})

def register_view(request):
    errors = {}

    next = ''
    if request.GET:
        next = request.GET['next']

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = User()
        profile = UserProfile()


        if full_name:
            profile.full_name = full_name
        else:
            errors['full_name'] = 'Name is required'

        if email:
            user.email = email
            user.username = email
            duplicate_email = User.objects.filter(email=email, username=email)
            if len(duplicate_email):
                errors['duplicate_email'] = 'Email is used'
        else:
            errors['email'] = 'Email is required'

        if not password:
            errors['password'] = 'Password is required'

        if not confirm_password:
            errors['confirm_password'] = 'Confirm password is required'

        if password != confirm_password:
            errors['invalid_password'] = 'Password does not match the confirm password'

        user.set_password(password)
        context = {
            'errors': errors,
        }

        if address:
            profile.address = address

        if phone_number:
            profile.phone_number = phone_number

        if len(errors):
            return render(request, "register.html", context)
        else:

            try:
                user.save()

            except Exception as e:
                errors['duplicate_username'] = 'This username is used'
                errors['python_error'] = str(e)
                return render(request, "register.html", context)

            profile.user = user
            profile.save()
            login(request, user, backend='user_managers.backends.EmailAuthenticationBackend')

            return HttpResponseRedirect('/users/')

    else:
        return render(request, "register.html", {'next': next})

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/login')
