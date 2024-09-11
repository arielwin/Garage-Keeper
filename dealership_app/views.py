from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Mod
from .forms import ServiceForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars':cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
    service_form = ServiceForm()
    return render(request, 'cars/detail.html', {
        'car':car, 
        'service_form': service_form, 
        'mods': mods_car_doesnt_have
    })

@login_required
def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('car-detail', car_id=car_id)

@login_required
def associate_mod(request, car_id, mod_id):
    Car.objects.get(id=car_id).mods.add(mod_id)
    return redirect('car-detail', car_id=car_id)

@login_required
def remove_mod(request, car_id, mod_id):
    car = Car.objects.get(id=car_id)
    car.mods.remove(mod_id)
    return redirect('car-detail', car_id=car.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = [
        'year',
        'make',
        'model',
        'price',
        'trans',
        'epa',
        'drivetrain',
        'engine',
        'intColor',
        'extColor',
        'vin',
        'description'
    ]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    fields = [
        'year',
        'make',
        'model',
        'price',
        'trans',
        'epa',
        'drivetrain',
        'engine',
        'intColor',
        'extColor',
        'vin',
        'description'
    ]

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/cars/'

class ModCreate(LoginRequiredMixin, CreateView):
    model = Mod
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ModList(LoginRequiredMixin, ListView):
    model = Mod

class ModDetail(LoginRequiredMixin, DetailView):
    model = Mod

class ModUpdate(LoginRequiredMixin, UpdateView):
    model = Mod
    fields = ['name','description']

class ModDelete(LoginRequiredMixin, DeleteView):
    model = Mod
    success_url = '/mods/'

    def test_func(self):
        mod = self.get_object()
        return self.request.user == mod.created_by

