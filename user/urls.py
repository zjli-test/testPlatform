from django.urls import path
from . import views
urlpatterns = [
    path('login', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    path('setpassword', views.setpasswordView, name='setpassword'),
    path('logout', views.logoutView, name='logout'),
]