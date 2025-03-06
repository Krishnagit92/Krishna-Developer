from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('order_foods', views.order_foods, name='order_foods'),
    path('register_form_submission', views.register_form_submission, name='register_form_submission')


]