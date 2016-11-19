from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^casereport/', views.casereport, name='casereport'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createcase/', views.managecases, name='managecases'),
    url(r'^createcase/complete/$', views.case_creation_complete,
 name='case_creation_complete'),
    url(r'^diagnose/', views.diagnose, name='diagnose'),
    url(r'^aetiology/', views.aetiology, name='aetiology'),
    url(r'^summary/', views.summary, name='summary'),
]