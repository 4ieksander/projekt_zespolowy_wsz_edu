from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.shortcuts import render, redirect

from .create_random_objects import CreateRandomOrganDonor
from .forms import SignUpForm, LoginForm, EditUserForm


@login_required
def home(request):          #strona główna
    # log.info(f"User {request.user} went to the homepage")
    return render(request, 'home.html')

def login_view(request):    #wbudowana funkcja login (dlatego login_view)
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # log.info(f"User {username} just logged in")
                return redirect('../')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):   #wbudowana funkcja logout (dlatego logout_view)
    logout(request)
    # log.info(f"User {request.user} just logged out")
    return redirect('../login/')

def signup(request):        #rejestracja
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # log.info(f"User {username} just registered")
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def create_random_organ_donor(request):
        create_random_organ_donor = CreateRandomOrganDonor()
        create_random_organ_donor.create_random_organ_donor()
        return redirect("../")