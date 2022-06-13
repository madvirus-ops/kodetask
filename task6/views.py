from django.shortcuts import render
from .forms import Hotel_Data_Form
from django.contrib import messages


# Create your views here.

def home(request):
	return render(request,'task6/home.html')

def about(request):
	return render(request,'task6/about.html')

def another(request):
	return render(request,'task6/another.html')

def hotel(request):
    if request.method == 'POST':
            form = Hotel_Data_Form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Form submission successful')
                return render(request, 'task6/hotel.html', {'form': form})

    else:
        form = Hotel_Data_Form()
    context ={
        'form':form,
        }
    return render(request,'task6/hotel.html',context)
        
