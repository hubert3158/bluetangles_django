from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'login-please'),
	# path('login/signup/registered/', views.registered),
	# path('signup/', views.signup ),

]