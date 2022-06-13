from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm,ProfileUpdateForm,NewProjectForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project
# from django.http  import HttpResponse

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

def Login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

            else:
                messages.error (request, 'Check username or password and try again')

        return render(request, 'authenticate/login.html' )

def UserLogout(request):

    logout(request)

    return redirect('login')

@login_required
def UserProfile(request):
    user=request.user

    return render(request, 'profile.html')

@login_required
def ProfileUpdate(request):
    if request.method == 'POST':
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'update_profile.html', context)

@login_required
def Project(request):
    user = request.user.id

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            url = form.cleaned_data.get('url')

            p = Project.objects.get_or_create(title=title, image=image,description=description,url=url, user_id=user)
            p.save()
            return redirect('home')
        else:
            form = NewProjectForm()
    else:
        form = NewProjectForm()
   
    
    return render(request, 'project.html',  {'form': form})



    
 