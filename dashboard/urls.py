from django.conf.urls import url, include
from . import views
from .views import toDoListViewSet, patientViewSet, caseViewSet
from rest_framework import routers

#for api
router = routers.DefaultRouter()
router.register(r'todolists', toDoListViewSet)
router.register(r'patients', patientViewSet)
router.register(r'cases', caseViewSet)

#for webapp
urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^casereport/', views.casereport, name='casereport'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^createcase/', views.createcase, name='createcase'),
    url(r'^diagnose/', views.diagnose, name='diagnose'),
    url(r'^sympadd/', views.sympadd, name='sympadd'),
    url(r'^sympremove/', views.sympremove, name='sympremove'),

    #FOR TESTING
    url(r'^diagnose1/', views.diagnose1, name='diagnose1'),
    url(r'^diagnose2/', views.diagnose2, name='diagnose2'),

    url(r'^profile/', views.profile, name='profile'),
    url(r'^aetiology/', views.aetiology, name='aetiology'),
    url(r'^summary/', views.summary, name='summary'),
]