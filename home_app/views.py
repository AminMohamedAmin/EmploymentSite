from django.shortcuts import render, HttpResponse
from .models import subscribes
from django.contrib import messages

# Create your views here.


def home_page(request):
    return render(request, 'homepage.html', {})

def gmail(request):
    return render(request, 'gmail.html', {})

def sub(request):
    subscriber = subscribes()
    em = request.POST['subs']
    try:
        if em is not None:
            if subscribes.objects.filter(email=em).exists() == True:
                messages.error(request, 'Already existed', extra_tags='error')
                return render(request, 'homepage.html', {})
            subscriber.email = request.POST['subs']
            subscriber.save()
            messages.success(request, 'Successfuly Saved', extra_tags='success')
            return render(request, 'homepage.html', {})
    except:
        messages.error(request, 'Failed Saved', extra_tags='error')
        return render(request, 'homepage.html', {})
