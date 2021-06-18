from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')


def process_money(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    earns = request.POST['earns']
    farm = random.randint(10, 20)
    cave = random.randint(5, 10)
    house = random.randint(2, 5)
    casino = random.randint(-50, 50)
    if earns == 'farm':
        request.session['gold'] += farm
        request.session['activities'].insert(0, f'Earned {farm} golds from the farm!')
    if earns == 'cave':
        request.session['gold'] += cave
        request.session['activities'].insert(0, f'Earned {cave} golds from the cave!')
    if earns == 'house':
        request.session['gold'] += house
        request.session['activities'].insert(0, f'Earned {house} golds from the house!')
    if earns == 'casino':
        request.session['gold'] += casino
        request.session['activities'].insert(0, f'Entered a casino and lost {casino} golds... Ouch...')
    return redirect('/')


def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')