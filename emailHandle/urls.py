from django.urls import path

from . import views

urlpatterns = [
	path('', views.sendgrid_parser, name = 'login-please'),
	

]