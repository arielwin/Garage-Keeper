from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('car/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),

]