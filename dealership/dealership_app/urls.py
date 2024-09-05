from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('car/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('cats/<int:car_id>/add-service/', views.add_service, name='add-service'),
    path('mods/create/', views.ModCreate.as_view(), name='mod-create'),
    path('mods/<int:pk>/', views.ModDetail.as_view(), name='mod-detail'),
    path('mods/', views.ModList.as_view(), name='mod-index'),
    path('mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mod-update'),
    path('mods/<int:pk>/delete/', views.ModDelete.as_view(), name='mod-delete'),
    path('accounts/signup/', views.signup, name='signup'),

]