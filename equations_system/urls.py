from django.urls import path
from equations_system import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("help/", views.help, name="help"),
    path('solve/', views.MyFormView.as_view(), name='solve'),
]