from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import CreateUserForm

import json
from decimal import Decimal


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            User.objects.create(
                user=user,
                username=user.username,
            )
            messages.success(request, f'User "{username.title()}" created')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong, please try again..')

    context = {
        'form': form,
    }

    return render(request, 'mainwebsite/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('mainwebsite_index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,
                                username=username,
                                password=password,
                                )
            if user is not None:
                login(request, user)
                return redirect('mainwebsite_index')
            else:
                messages.error(request, 'Username of password is incorrect')

    context = {}

    return render(request, 'mainwebsite/login.html', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    user = User.objects.get(user=request.user)

    labels = ['win', 'lose', 'draw']
    data = [user.win, user.lose, user.draw]

    context = {
        'labels': labels,
        'data': data
    }

    return render(request, 'mainwebsite/index.html', context)


@login_required(login_url='login')
def add_funds(request):
    return render(request, 'mainwebsite/add_funds.html')


@login_required(login_url='login')
def deposit(request, amount):
    user = get_object_or_404(User, user=request.user)
    available_amounts = [50, 150, 500]

    if amount in available_amounts:
        context = {
            'user': user,
            'amount': amount
        }
        return render(request, 'mainwebsite/checkout.html', context)
    else:
        return redirect('mainwebsite_index')


@login_required(login_url='login')
def deposit_complete(request):
    user = User.objects.get(user=request.user)

    try:
        body = json.loads(request.body)

        if user.username == body['user']:
            user.money += Decimal(body['amount'])
            user.save()
            return redirect('mainwebsite_index')
    except:
        return redirect('mainwebsite_index')