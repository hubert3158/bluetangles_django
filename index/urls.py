from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'login-please'),
	path('registration/', views.registration),
	path('<str:inpvalue>/', views.redirector)
	# path('login/signup/registered/', views.registered),
	# path('signup/', views.signup ),

]