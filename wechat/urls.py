from django.urls import path
from . import views
app_name='wechat'
urlpatterns = [
    path(r'^$', views.weixin_main, name='weixin_main'),
]