from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from mainwebsite.models import User
from .forms import LevelEasy, LevelNormal, LevelHard

from decimal import Decimal
import random


@login_required(login_url='login')
def level_choice(request):
    context = {}

    return render(request, 'guessnumber/level_choice.html', context)


@login_required(login_url='login')
def level_easy(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')
    multiplier = Decimal(1.25)
    expected_number = random.randint(1, 5)

    form = LevelEasy()
    if request.method == "POST":
        form = LevelEasy(request.POST)
        if form.is_valid():
            bet_amount = form.cleaned_data['bet_amount']
            given_number = form.cleaned_data['given_number']

            if user.money >= bet_amount:
                user.money -= bet_amount
                user.save()
                if expected_number == given_number:
                    user.money += bet_amount + (bet_amount * multiplier)
                    user.win += 1
                    user.save()

                    main_account.money -= (bet_amount * multiplier)
                    main_account.lose += 1
                    main_account.save()
                    messages.success(request, f'You won {bet_amount * multiplier}!')
                else:
                    messages.error(request, f'Sorry, not this time.. Lucky number: {expected_number}')
                    main_account.money += bet_amount
                    main_account.win += 1
                    main_account.save()

                    user.lose += 1
                    user.save()
            else:
                messages.error(request, "You don't have enough money")

    context = {
        'form': form
    }

    return render(request, 'guessnumber/play_level_easy.html', context)


@login_required(login_url='login')
def level_normal(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')
    multiplier = 2
    expected_numbers = []
    correct_numbers = []

    for i in range(2):
        number = random.randint(1, 10)
        if number in expected_numbers:
            while True:
                number = random.randint(1, 10)
                if number not in expected_numbers:
                    expected_numbers.append(number)
                    break
        else:
            expected_numbers.append(number)

    form = LevelNormal()
    if request.method == "POST":
        form = LevelNormal(request.POST)
        if form.is_valid():
            bet_amount = form.cleaned_data['bet_amount']
            given_number_1 = form.cleaned_data['given_number_1']
            given_number_2 = form.cleaned_data['given_number_2']

            if user.money >= bet_amount:
                user.money -= bet_amount
                user.save()
                given_list = [given_number_1, given_number_2]

                for i in expected_numbers:
                    for j in given_list:
                        if i == j:
                            correct_numbers.append(j)

                if len(correct_numbers) == 2:
                    messages.success(request, 'You won! Correctly guessed two number!')
                    user.money += bet_amount + (bet_amount * multiplier)
                    user.win += 1
                    user.save()

                    main_account.money -= (bet_amount * multiplier)
                    main_account.lose += 1
                    main_account.save()

                elif len(correct_numbers) == 1:
                    messages.info(request, 'Was close... Your bet amount is got back')
                    user.money += bet_amount
                    user.draw += 1
                    user.save()

                    main_account.draw += 1
                    main_account.save()
                else:
                    messages.error(request, f'You lose, maybe next time! Lucky numbers {expected_numbers}')
                    main_account.money += bet_amount
                    main_account.win += 1
                    main_account.save()

                    user.lose += 1
                    user.save()
            else:
                messages.error(request, "You don't have enough money")

    context = {
        'form': form,
    }

    return render(request, 'guessnumber/play_level_normal.html', context)


@login_required(login_url='login')
def level_hard(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')
    multiplier = 10
    expected_numbers = []
    lucky_number = random.randint(1, 5)
    correct_numbers = []

    for i in range(2):
        number = random.randint(1, 15)
        if number in expected_numbers:
            while True:
                number = random.randint(1, 15)
                if number not in expected_numbers:
                    expected_numbers.append(number)
                    break
        else:
            expected_numbers.append(number)

    form = LevelHard()
    if request.method == "POST":
        form = LevelHard(request.POST)
        if form.is_valid():
            bet_amount = form.cleaned_data['bet_amount']
            given_number_1 = form.cleaned_data['given_number_1']
            given_number_2 = form.cleaned_data['given_number_2']
            given_lucky_number = form.cleaned_data['lucky_number']

            if user.money >= bet_amount:
                user.money -= bet_amount
                user.save()
                given_list = [given_number_1, given_number_2]

                for i in expected_numbers:
                    for j in given_list:
                        if i == j:
                            correct_numbers.append(j)

                if len(correct_numbers) == 2 and lucky_number == given_lucky_number:
                    messages.success(request, 'You won! Correctly guessed two number and special number!')
                    user.money += bet_amount + (bet_amount * multiplier)
                    user.win += 1
                    user.save()

                    main_account.money -= (bet_amount * multiplier)
                    main_account.lose += 1
                    main_account.save()
                elif len(correct_numbers) == 2:
                    messages.info(request, 'Was close... Your bet amount is got back')
                    user.money += bet_amount
                    user.draw += 1
                    user.save()

                    main_account.draw += 1
                    main_account.save()
                else:
                    messages.error(request, f'You lose, maybe next time! Lucky numbers {expected_numbers}')
                    main_account.money += bet_amount
                    main_account.win += 1
                    main_account.save()

                    user.lose += 1
                    user.save()
            else:
                messages.error(request, "You don't have enough money")

    context = {
        'form': form
    }

    return render(request, 'guessnumber/play_level_hard.html', context)
