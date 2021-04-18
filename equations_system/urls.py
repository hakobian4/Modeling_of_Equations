from django.urls import path
from equations_system import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("page/", views.page, name="page"),
    path('class-form/', views.MyFormView.as_view(), name='class_form'),
]