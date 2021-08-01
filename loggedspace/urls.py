from django.urls import path

from . import views

urlpatterns = [
	path('', views.loggedspace, name = 'Welcome'),
]