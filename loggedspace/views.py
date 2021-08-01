from django.shortcuts import render

# Create your views here.

def loggedspace(request):
	return render(request, 'loggedspace/loggedspace.html')