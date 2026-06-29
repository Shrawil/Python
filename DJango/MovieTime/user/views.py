from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()      # Creates the user
            login(request, user)    # Logs them in
            return redirect('index')

    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    #Check if the request method is POST or not.
    if request.method == "POST":
        #If true, store username and password to authenticate
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Authenticate the username and password (Check whether the credentials are valid or not)
        user = authenticate(request, username=username, password=password)

        #If the user is valid it will not be None so we can check.
        if user is not None:
            # Log that user in and redirect them to home page
            login(request, user)
            return redirect('index')

        #If we reach this area, that means user entered invalid credentials
        return render(request, 'accounts/login.html', {'error':'Invalid credentials!'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')