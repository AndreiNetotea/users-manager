from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserForm
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


class UserListView(ListView):
    model = UserProfile
    template_name = 'class_users_list.html'
    context_object_name = 'books'


class UploadCvView(CreateView):
    model = UserProfile
    form_class = UserForm
    success_url = reverse_lazy('class_users_list')
    template_name = 'ad_cv.html'