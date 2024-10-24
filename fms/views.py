from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import newfile
from django.contrib.auth.models import User
from .decorators import role_required
from datetime import datetime
from django.utils import timezone


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            print("User logged in successfully")  # Add this line for debugging
            if request.user.is_staff:
                return redirect('admin_login')  # Assuming you have a named URL for admin dashboard  # Assuming you have a named URL for office staff dashboard
            elif user.groups.filter(name='PRINCIPAL').exists():
                return redirect('principal_dashbord')
              
            elif user.groups.filter(name='SUPERINTENDENT').exists():
                return redirect('superintendent_dashbord')
            
            elif user.groups.filter(name='STAFFS').exists():
                return redirect('user_dashbord')
            else:
                messages.error(request, "User role not defined.")
                return redirect('login')  # Handle case where user doesn't belong to any defined role
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, "login.html")
     

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request,"about.html")


# @role_required('SUPERINTENDENT')
def superintendent_view(request):
    context = {}  # Define context here
    if request.method == 'POST':
        section = request.POST['section']
        newfiles = newfile()
        newfiles.reciver = section
        newfiles.senders='Superintendent'
        newfiles.created_date=datetime.now() 
        newfiles.save()
        context = {'newfile': newfiles}
        messages.success(request, 'Succes')        
    
    usernames = User.objects.filter(is_superuser=False).values_list('username', flat=True)
    context['usernames'] = usernames

    # Get the count of new files where sender and logged-in user match
    logged_in_username = request.user.username
    newfile_count = newfile.objects.filter(senders=logged_in_username).count()
    pendingfile_count = newfile.objects.filter(reciver=logged_in_username).count()
    total=newfile_count+pendingfile_count
    context['newfile_count'] = newfile_count
    context['pendingfile_count']=pendingfile_count
    context['total']=total
    return render(request,'superintendent.html',context)

# @role_required('PRINCIPAL')
def princi(request):
    context = {}  # Define context here
    if request.method == 'POST':
        section = request.POST['section']
        newfiles = newfile()
        newfiles.reciver = section
        newfiles.senders='Principal'
        newfiles.created_date=timezone.now()
        newfiles.save()
        context = {'newfile': newfiles}
        messages.success(request, 'Succes')        
    
    usernames = User.objects.filter(is_superuser=False).values_list('username', flat=True)
    context['usernames'] = usernames
    # file = {'newfile': newfiles}

     # Get the count of new files where sender and logged-in user match
    logged_in_username = request.user.username
    newfile_count = newfile.objects.filter(senders=logged_in_username).count()
    pendingfile_count = newfile.objects.filter(reciver=logged_in_username).count()
    total=newfile_count+pendingfile_count
    context['newfile_count'] = newfile_count
    context['pendingfile_count']=pendingfile_count
    context['total']=total

    return render(request, 'principal.html', context)

# @role_required('STAFFS')
def staff_view(request):
    # Get the count of new files where sender and logged-in user match
    context = {}

    logged_in_username = request.user.username
    pendingfile_count = newfile.objects.filter(reciver=logged_in_username).count()
    context['pendingfile_count']=pendingfile_count
    return render(request,'user.html',context)


def new_files_created(request):
    logged_in_username = request.user.username
    
    # Filter newfiles to show only the records where reciver and username are the same
    newfiles = newfile.objects.filter(senders=logged_in_username)
    newfile_count = newfiles.count()
    
    context = {'newfiles': newfiles,'newfiles_count' : newfile_count}
    return render(request, 'new_files.html', context)


def dashboard_redirect(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='SUPERINTENDENT').exists():
            return redirect('superintendent_dashbord')
        elif request.user.groups.filter(name='PRINCIPAL').exists():
            return redirect('principal_dashbord')
        else:
            return redirect('user_dashbord')
    else:
        return redirect('login')  # Redirect to the login page if not authenticated


def pending_file(request):
    logged_in_username = request.user.username
    
    # Filter newfiles to show only the records where reciver and username are the same
    newfiles = newfile.objects.filter(reciver=logged_in_username)
    
    context = {'newfiles': newfiles}
    return render(request, 'pending_files.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home_page')
