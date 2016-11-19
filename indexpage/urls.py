from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpg, name='mainpg'),
    url(r'^register/', views.register, name='register'),
    url(r'^signin/', views.signin, name='signin'),
]