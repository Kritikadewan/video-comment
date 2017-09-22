from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^index$', views.index, name='index'),	
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^$', views.index, name='index'),
]