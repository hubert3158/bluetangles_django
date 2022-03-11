from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# Create your views here. 

def index(request):

	if request.user.is_authenticated:
			return redirect("/loggedspace/")

	if request.method == 'POST':
		# return redirect("/loggedspace/")
		username = request.POST['usernamea']
		password = request.POST['passworda']

		user = authenticate(request,username=username,password=password)
		# user = authenticate(request,username=username,password=password)


			

		if user is not None:
			auth.login(request, user)
			return redirect("/loggedspace/")
		else:
			messages.info(request,'invalid credentials')
			# return redirect("loggedspace/")
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

	else:
		return render(request, 'index/index.html')


def redirector(request, inpvalue):
	if inpvalue == 'login' or inpvalue == 'index' :
		return redirect('/')
	elif inpvalue == 'signup':
		return redirect('/registration/')
	elif inpvalue == 'logout':
		 logout(request)
		 return redirect('/')
	else:
		return render(request, 'index/'+inpvalue+'.html')


def registration(request):

	# return redirect("/test/")

	if request.method == 'POST':
		# return redirect("/test/")
		fname = request.POST['fname']
		lname = request.POST['lname']
		username = request.POST['username']
		regemail = request.POST['regemail']
		regpassword = request.POST['regpassword']
		


		try:
			user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=regemail,password=regpassword)
			user.save();
			
		except: 
			messages.info(request,'Please re-check the information')
			# return redirect("loggedspace/")
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
		else:
			return redirect('registered/')
		# user = auth.authenticate(email=email,password=password)

		# if user is not None:

		# 	auth.login(request,user)
		# 	return redirect("loggedspace/")
		# else:
		# 	messages.info(request,'invalid credentials')
		# 	return redirect('/hahahaha')

		# print('user created')
		# return redirect('/admin/')

	else:

		return render(request, 'index/registration.html')


# def login(request):
# 	if request.method == 'POST':

# 		email = request.POST['email']
# 		password = request.POST['password']

# 		user = auth.authenticate(email=email,password=password)
# 		if user is not None:
# 			auth.login(request,user)
# 			return redirect("loggedspace/")
# 		else:
# 			messages.info(request,'invalid credentials')
# 			return redirect('loggedspace/')

# 	else:
# 		return render(request, 'index/index.html')


# def registered(request):

# 	return render(request, 'index/registered.html')