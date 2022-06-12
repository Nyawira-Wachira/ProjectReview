from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib import messages

# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = RegisterUserForm()
        if request.method =='POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account Created Successfully! You are now able to log in")

                return redirect('login')


        return render(request, 'authenticate/register.html',{'form':form} )