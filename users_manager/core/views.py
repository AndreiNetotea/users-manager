from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Appointment, Job
from .forms import UserForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def add_user(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'ad_user.html', context)

@login_required()
def users_list(request):
    users = UserProfile.objects.all()
    return render(request, 'users_list.html', {
        'users': users
    })

@login_required()
def upload_cv(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'ad_cv.html', {
        'form': form
    })


@login_required()
def delete_user(request, pk):
    if request.method == 'POST':
        user = UserProfile.objects.get(pk=pk)
        user.delete()
    return redirect('users_list')


@login_required()
def user_details(request, id):
    context = {}
    try:
        context['user'] = UserProfile.objects.get(id=id)
    except:
        return HttpResponseRedirect('/users')
    print(context)
    return render(request, 'user_details.html', context)


@login_required
def profile_page(request, context={}):

    if request.method == 'POST':
        errors = {}
        update = False

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user
        profile = request.user.profile

        if email != user.email:
            update = True
            user.email = email
            user.username = email
            duplicate_email = User.objects.filter(email=email, username=email)
            if len(duplicate_email):
                errors['duplicate_email'] = 'Email is used'

        if full_name != profile.full_name:
            update = True
            profile.full_name = full_name

        if phone_number != profile.phone_number:
            update = True
            profile.phone_number = phone_number

        if address != profile.address:
            update = True
            profile.address = address

        if password or confirm_password:
            if password != confirm_password:
                errors['invalid_password'] = 'Password does not match the confirm password'
            else:
                update = True
                user.set_password(password)

        if len(errors):
            context['errors'] = errors
            return render(request, 'profile_page.html', context)
        else:

            try:
                if update:
                    user.save()
                    profile.save()

            except Exception as e:
                errors['python_error'] = str(e)
                context['errors'] = errors
                return render(
                    request, 'profile_page.html', context)

            return HttpResponseRedirect('/profile-page')

    else:
        return render(request, 'profile_page.html', context)



@login_required()
def jobs(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs.html', {
        'jobs': jobs
    })


@login_required
def add_job(request):
    errors = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        location = request.POST.get('location')

        job = Job()

        if not name:
            errors['name'] = 'Numele este obligatoriu'

        if not description:
            errors['description'] = 'Descrierea este obligatorie'

        if not salary:
            errors['salary'] = 'Salariul este obligatoriu'

        if len(errors):
            return render(request, 'add-job.html', {
                'errors': errors,
                'name': name,
                'description': description,
                'salary': salary,
                'location': location
            })
        else:
            try:
                job.user = request.user
                job.name = name
                job.description = description
                job.salary = salary
                job.location = location
                job.save()

            except Exception as e:
                raise e
                return render(request, 'add-job.html', {
                    'errors': errors,
                    'name': name,
                    'description': description,
                    'salary': salary,
                    'location': location
                })

            return HttpResponseRedirect('/jobs')

    else:
        return render(request, 'add-job.html')


@login_required()
def appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments.html', {
        'appointments': appointments
    })


@login_required
def add_appointment(request):
    errors = {}
    profiles = UserProfile.objects.filter(user=request.user)
    jobs = Job.objects.filter(user=request.user)

    if request.method == 'POST':
        profile = request.POST.get('profile')
        job = request.POST.get('job')
        date = request.POST.get('date')
        notes = request.POST.get('notes')
        appointment = Appointment()

        if not profile:
            errors['profile'] = 'Profilul este obligatoriu'

        if not job:
            errors['job'] = 'Jobul este obligatoriu'

        if not date:
            errors['date'] = 'Data este obligatorie'

        if len(errors):
            return render(request, 'add-appointment.html', {
                'errors': errors,
                'profile': profile,
                'job': job,
                'date': date,
                'notes': notes,
                'jobs': jobs,
                'profiles': profiles
            })
        else:
            try:
                appointment.user = request.user
                appointment.profile = UserProfile.objects.get(id=profile)
                appointment.job = Job.objects.get(id=job)
                appointment.date = date
                appointment.notes = notes
                appointment.save()

            except Exception as e:
                raise e
                return render(request, 'add-appointment.html', {
                    'errors': errors,
                    'profile': profile,
                    'job': job,
                    'date': date,
                    'notes': notes,
                    'jobs': jobs,
                    'profiles': profiles
                })

            return HttpResponseRedirect('/appointments')

    else:
        return render(request, 'add-appointment.html', {
            'jobs': jobs,
            'profiles': profiles
        })


class UserListView(ListView):
    model = UserProfile
    template_name = 'class_users_list.html'
    context_object_name = 'books'


class UploadCvView(CreateView):
    model = UserProfile
    form_class = UserForm
    success_url = reverse_lazy('class_users_list')
    template_name = 'ad_cv.html'