from django.urls import path
from . import views

urlpatterns = [
    path('count/<int:angka>/', views.count),
    path('example/', views.example),
    path('shop/', views.shop),
    path('first/', views.first),
    path('second/', views.second),
    path('profile/', views.profile),
    path('second/', views.second_page),
    path('', views.landing_page)

]