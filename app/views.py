from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	# return HttpResponse("Hello World")
	return render(request, "index.html", {})

def about(request):
	return render(request, "about.html", {})

def portfolio(request):
	return render(request, "portfolio.html", {})

def contact(request):
	return render(request, "contact.html", {})