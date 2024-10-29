from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Card


def index(request):
    cards = Card.objects.all().order_by('name')
    context = {'cards': cards,
               'columns': ['image', 'name', 'cost', 'power', 'description', 'pool', 'owned', 'submit'],
               'sortable_columns': ['name', 'cost', 'power', 'pool', 'owned']
    }
    return render(request, 'snap/index.html', context)


def stats(request):
    cards = Card.objects.all()
    owned_rates = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    pools = ['Starter', 'Recruit', 'Pool 1', 'Pool 2', 'Pool 3', 'Pool 4', 'Pool 5', 'All']

    for card in cards:
        if card.pool == 'starter':
            owned_rates[0][1] += 1
            if card.owned == True: owned_rates[0][0] += 1
        elif card.pool == 'recruit':
            owned_rates[1][1] += 1
            if card.owned == True: owned_rates[1][0] += 1
        elif card.pool == '1':
            owned_rates[2][1] += 1
            if card.owned == True: owned_rates[2][0] += 1
        elif card.pool == '2':
            owned_rates[3][1] += 1
            if card.owned == True: owned_rates[3][0] += 1
        elif card.pool == '3':
            owned_rates[4][1] += 1
            if card.owned == True: owned_rates[4][0] += 1
        elif card.pool == '4':
            owned_rates[5][1] += 1
            if card.owned == True: owned_rates[5][0] += 1
        elif card.pool == '5':
            owned_rates[6][1] += 1
            if card.owned == True: owned_rates[6][0] += 1
        if card.pool != 'none':
            owned_rates[7][1] += 1
            if card.owned == True: owned_rates[7][0] += 1

    context = {'cards': cards,
               'owned_rates': owned_rates,
               'pools': pools
    }
    return render(request, 'snap/stats.html', context)


def toggle_owned(request, card_name):
    card = get_object_or_404(Card, pk=card_name)
    if request.POST.get('owned') == 'on': card.owned = True
    else: card.owned = False
    card.save()
    return HttpResponseRedirect(reverse('snap:index'))


def add_card(request):
    card = Card(
        name = request.POST.get('name'),
        image = request.FILES['image'],
        cost = request.POST.get('cost'),
        power = request.POST.get('power'),
        description = request.POST.get('description'),
        pool = request.POST.get('pool'),
        owned = True if request.POST.get('owned') == 'on' else False
    )
    card.save()
    return HttpResponseRedirect(reverse('snap:index'))