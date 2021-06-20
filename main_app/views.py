from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')


def process_money(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    earns = request.POST['earns']
    date = strftime("%Y/%m/%d", gmtime())
    time = strftime("%I:%M %p", gmtime())
    clase = 1
    gold = 0
    if earns == 'farm':
        gold = random.randint(10, 20)
        request.session['gold'] += gold
    elif earns == 'cave':
        gold = random.randint(5, 10)
        request.session['gold'] += gold
    elif earns == 'house':
        gold = random.randint(2, 5)
        request.session['gold'] += gold
    elif earns == 'casino':
        gold = random.randint(-50, 50)
        if gold > 0:
            request.session['gold'] += gold
        elif gold < 0:
            request.session['gold'] += gold
            clase = 0
        else:
            request.session['gold'] += gold
            clase = 2
    message = f"Earned {gold} golds from the {earns}! ({date} {time})"
    if gold < 0:
        message = f"Entered a gold and lost {gold} golds... Ouch... ({date} {time})"
    elif gold == 0:
        message = f"Entered in a void, don't win and don't lose ({date} {time})"
    activitiesobject = {
        'clase': clase,
        'message': message
    }
    request.session['activities'].insert(0, activitiesobject)
    return redirect('/')


def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')