from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('blog.html', views.blog, name="blog"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('single.html', views.single, name="single"),
    path('team.html', views.team, name="team"),
    path('appointment.html', views.appointment, name="appointment"),
]