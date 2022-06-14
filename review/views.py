from urllib import request
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm,ProfileUpdateForm,NewProjectForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from django.template import loader
from django.urls import reverse, resolve
from django.http import HttpResponse, HttpResponseRedirect

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
    from .models import Project
    user=request.user
    projects= Project.objects.filter(user=user).order_by('-posted')


    return render(request, 'profile.html',{'projects':projects} )


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

def search_results(request):
    from .models import Project

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required
def ProjectDetails(request, project_id):
    from .models import Project
    project = Project.objects.get(id=project_id)
    user = request.user

    return render(request, 'project_details.html',{'project':project})

def home(request):
    from .models import Project
    user=request.user

    project_items = Project.objects.all().order_by('-posted')

    template=loader.get_template('home.html')

    context= {
        'project_items': project_items,

    }

    return HttpResponse(template.render(context, request))    
   
    
	
