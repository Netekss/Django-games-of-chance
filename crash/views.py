from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CrashForm
from .models import CrashPlayer
from mainwebsite.models import User

import random


def random_crash():
    x = ['win', 'lose', 'win']
    return random.choice(x)


@login_required(login_url='login')
def crash_bet(request):
    user = User.objects.get(user=request.user)

    try:
        player_profile = CrashPlayer.objects.get(user=user)
        return redirect('crash_play')

    except:
        form = CrashForm()
        if request.method == "POST":
            form = CrashForm(request.POST)
            if form.is_valid():
                bet_amount = form.cleaned_data['bet_amount']

                if user.money >= bet_amount:
                    user.money -= bet_amount
                    user.save()

                    player_profile = CrashPlayer.objects.create(user=user,
                                                                bet=bet_amount,
                                                                attempt=0,
                                                                )
                    player_profile.save()
                    return redirect('crash_play')
                else:
                    messages.error(request, "You don't have enough money")

        context = {
            'form': form,
        }

        return render(request, 'crash/bet.html', context)


@login_required(login_url='login')
def crash_game(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')

    try:
        player_profile = CrashPlayer.objects.get(user=user)

        if player_profile.attempt < 6:

            crash = random_crash()

            if crash == 'win':
                player_profile.attempt += 1
                player_profile.save()
            else:
                main_account.money += player_profile.bet
                main_account.win += 1
                main_account.save()

                user.lose += 1
                user.save()

                player_profile.delete()

                messages.error(request, 'lose, try again')
                return redirect('crash_bet')

            context = {
                'player_profile': player_profile
            }

            return render(request, 'crash/game.html', context)

        else:
            bet_money = player_profile.bet
            attempts = player_profile.attempt

            money_to_return = attempts * bet_money + bet_money

            main_account.money -= attempts * bet_money
            main_account.lose += 1
            main_account.save()

            user.money += money_to_return
            user.win += 1
            user.save()

            player_profile.delete()

            messages.success(request, 'You won this game! Good job!')
            return redirect('mainwebsite_index')

    except:
        return redirect('crash_bet')


@login_required(login_url='login')
def take_money(request):
    user = User.objects.get(user=request.user)
    main_account = User.objects.get(username='admin')

    try:
        player_profile = CrashPlayer.objects.get(user=user)

        if player_profile.attempt >= 1:
            bet_money = player_profile.bet
            attempts = player_profile.attempt

            money_to_return = attempts * bet_money + bet_money

            main_account.money -= attempts * bet_money
            main_account.lose += 1
            main_account.save()

            user.money += money_to_return
            user.win += 1
            user.save()

            player_profile.delete()

            messages.success(request, f'You won in this game {attempts * bet_money}$')
            return redirect('mainwebsite_index')

    except:
        return redirect('mainwebsite_index')
