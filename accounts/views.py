from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .admin import PurBeurreUserCreationForm


@login_required(login_url="/accounts/login/")
def my_account_view(request):
    return render(request, 'accounts/account.html')


def signup_view(request):
    if request.method == 'POST':
        form = PurBeurreUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log in the user
            accounts_user = form.save()
            login(request, accounts_user)

            return redirect('main:index')
    else:
        form = PurBeurreUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            # Reroute the user to the previous page after log in
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # Message
                messages.success(request, 'Bonjour!')

                return redirect('main:index')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url="/accounts/login/")
def logout_view(request):
    logout(request)
    template = loader.get_template('main/index.html')
    # Message
    messages.success(request, 'Bye bye amigo!')

    return HttpResponse(template.render(request=request))
