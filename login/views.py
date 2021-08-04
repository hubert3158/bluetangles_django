from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here. 

def index(request):
	if request.method == 'POST':
		# return redirect("/loggedspace/")
		username = request.POST['usernamea']
		password = request.POST['passworda']

		# user = auth.authenticate(username=username,password=password)
		user = authenticate(request,username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/loggedspace/")
		else:
			messages.info(request,'invalid credentials')
			# return redirect("loggedspace/")
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

	# else:
	# 	return render(request, 'login/index.html')

# def signup(request):

	# if request.method == 'POST':
		
		fname = request.POST['fname']
		lname = request.POST['lname']
		username = request.POST['username']
		regemail = request.POST['regemail']
		regpassword = request.POST['regpassword']
		
		try:
			user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=regemail,password=regpassword)
			user.save();
		except: 
			# return redirect(request.META.get('	', 'redirect_if_referer_not_found'))
			return redirect('')
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

		return render(request, 'login/index.html')


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
# 		return render(request, 'login/index.html')


def registered(request):

	return render(request, 'login/registered.html')