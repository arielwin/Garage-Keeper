from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Mod
from .forms import ServiceForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars':cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    service_form = ServiceForm()
    return render(request, 'cars/detail.html', {
        'car':car, 'service_form': service_form
    })

def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('car-detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

class ModCreate(CreateView):
    model = Mod
    fields = '__all__'

class ModList(ListView):
    model = Mod

class ModDetail(DetailView):
    model = Mod

class ModUpdate(UpdateView):
    model = Mod
    fields = ['name','description']

class ModDelete(DeleteView):
    model = Mod
    success_url = '/mods/'

