from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm


def login_view(request):
    context = {}
    # user = request.user
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('dashboard')
    # if user.is_authenticated:
    #     return redirect('dashboard')

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'login/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            auth_login(request, account)
            return redirect('home')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'register/register.html', context)
