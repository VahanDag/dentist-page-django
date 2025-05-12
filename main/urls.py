from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('iletisim/', views.contact, name="contact"),
    path('randevu-al/', views.randevu, name="randevu"),
]