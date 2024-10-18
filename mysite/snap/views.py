from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Card


def index(request, sort_column=None, sort_type='asc'):
    cards = Card.objects.all()
    if sort_column:
        if sort_type == 'desc':
            sort_column = '-' + sort_column
        cards = cards.order_by(sort_column)
    owned_rates = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],[0, 0]]
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
        elif card.pool == 'none':
            owned_rates[7][1] += 1
            if card.owned == True: owned_rates[7][0] += 1
    context = {'cards': cards,
               'owned_rates': owned_rates,
               'columns': ['image', 'name', 'cost', 'power', 'description', 'pool', 'owned', 'submit'],
               'sortable_columns': ['name', 'cost', 'power', 'pool', 'owned']
               }
    return render(request, 'snap/index.html', context)


# add try/except/else
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


# def sort_cards(request, sort_column, sort_type):
#     return HttpResponseRedirect(reverse('snap:index', args=[sort_column, sort_type]))