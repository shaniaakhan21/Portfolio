from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            name,
            message,
            email,
            ['shaniaakhan21@gmail.com']
        )

        return render(request,'portfolio/index.html', {'name':name })
    else:
        return render(request, 'portfolio/index.html',{}) 

