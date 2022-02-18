from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def userRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            msg = "UserName Already taken, Please try with another name..."
            messages.error(request, msg)
        elif User.objects.filter(email=email).exists():
            msg = "Email already exists"
            messages.error(request, msg)
        elif password1 != password2:
            msg = "Passwords are not matching, Please check"
            messages.error(request, msg)
        else:
            user = User.objects.create(username=username, email=email, password=password1)
            user.save()
            msg = "User Registered Successfully"
            messages.success(request, msg)
        return redirect('user.registration')
    else:
        return render(request, 'registration/register.html')