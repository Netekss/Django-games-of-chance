# Django-games_of_chance
## Django app with gambling and games of chance 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [To Do](#to-do)

## General info
Web application allows user to bet money in couple games, and win prizes

In this web application you can:
* create account
* login
* add funds to account via PayPal (sendbox)
    * I didn't create PayPal account so API key is default
    * If transaction is successful user will get payment amount added to his account in database,
    equivalent of token.
* play two simple different games:
    * guess number 
    * crash (every click is chance to get more money or lose all bet amount)
* see the ratio of win to lose

## Technologies
Project is created with:
* Python 3.8
* Django 3.1.3
* Bootstrap 4
* PayPal
	
## Setup
To run this project on Windows:
* pip install virtualvenv (for keep order)
* py -m venv myvenv
* myvenv\scripts\activate
* pip install -r requirements.txt
* py manage.py runserver

On Linux/Ubuntu:
* sudo apt install python-pip
* sudo apt install virtualenv (for keep order)
* virtualenv myvenv
* source myvenv/bin/activate
* pip install -r requirements.txt
* python manage.py runserver

## To Do:
* add hangman game
* create money withdrawal module