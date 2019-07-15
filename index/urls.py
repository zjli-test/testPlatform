from django.urls import path
from . import views
urlpatterns = [
    path('index', views.indexView, name='index'),
    path('userInfo',views.userInfo_list,name='userInfo'),
    path('add_user',views.add_user,name='add_user'),
]