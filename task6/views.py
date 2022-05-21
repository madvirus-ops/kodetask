from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'task6/home.html')

def about(request):
	return render(request,'task6/about.html')

def another(request):
	return render(request,'task6/another.html')