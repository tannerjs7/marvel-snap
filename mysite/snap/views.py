from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Q
from .models import Card, Spotlight, Deck
from django.contrib.auth.decorators import login_required


def index(request, filter=None):
    if filter == 'owned': cards = Card.objects.filter(owned=True)
    elif filter == 'unowned': cards = Card.objects.filter(owned=False, released=True).exclude(pool='none')
    elif filter == 'released': cards = Card.objects.filter(released=True).exclude(pool='none')
    elif filter == 'unreleased': cards = Card.objects.filter(released=False)
    elif filter == 'none': cards = Card.objects.filter(pool='none')
    elif filter == 'starter': cards = Card.objects.filter(Q(pool='starter') | Q(pool='recruit'))
    elif filter: cards = Card.objects.filter(pool=filter)
    else: cards = Card.objects.filter(~Q(pool='none'))
    context = {
        'cards': cards,
        'columns': ['image', 'name', 'cost', 'power', 'description', 'pool', 'released', 'owned', 'submit'],
        'filter': filter
    }
    return render(request, 'snap/index.html', context)


def stats(request):
    cards = Card.objects.all()
    owned_rates = [[0, 0, 0] for _ in range(7)]
    pools = ['Starter/Recruit', 'Pool 1', 'Pool 2', 'Pool 3', 'Pool 4', 'Pool 5', 'All']

    for card in cards:
        if card.released:
            if card.pool == 'starter' or card.pool =='recruit':
                owned_rates[0][1] += 1
                if card.owned == True: owned_rates[0][0] += 1
            elif card.pool == '1':
                owned_rates[1][1] += 1
                if card.owned == True: owned_rates[1][0] += 1
            elif card.pool == '2':
                owned_rates[2][1] += 1
                if card.owned == True: owned_rates[2][0] += 1
            elif card.pool == '3':
                owned_rates[3][1] += 1
                if card.owned == True: owned_rates[3][0] += 1
            elif card.pool == '4':
                owned_rates[4][1] += 1
                if card.owned == True: owned_rates[4][0] += 1
            elif card.pool == '5':
                owned_rates[5][1] += 1
                if card.owned == True: owned_rates[5][0] += 1
            if card.pool != 'none':
                owned_rates[6][1] += 1
                if card.owned == True: owned_rates[6][0] += 1

    for rate in owned_rates:
        rate[2] = rate[0] / rate[1] * 100
        if rate[2] == 100: rate[2] = 100
        else: rate[2] = round(rate[2], 1)

    context = {
        'cards': cards,
        'owned_rates': owned_rates,
        'pools': pools
    }
    return render(request, 'snap/stats.html', context)


def spotlights(request):
    context = {
        'spotlights': Spotlight.objects.all().order_by('-date'),
        'cards': Card.objects.filter(~Q(pool='none')).order_by('name'),
        'slots': range(1, 5)
    }
    return render(request, 'snap/spotlights.html', context)


def packs(request):
    context = {}
    return render(request, 'snap/packs.html', context)


@login_required
def decks(request):
    context = {
        'decks': Deck.objects.all(),
        'cards': Card.objects.filter(~Q(pool='none')).order_by('name')
    }
    return render(request, 'snap/decks.html', context)


@login_required
def toggle_checkboxes(request, card_name):
    card = get_object_or_404(Card, pk=card_name)
    if request.POST.get('owned') == 'on': card.owned = True
    else: card.owned = False
    if request.POST.get('released') == 'on': card.released = True
    else: card.released = False
    card.save()
    return HttpResponseRedirect(reverse('snap:index'))


@login_required
def add(request):
    context = {
        'cards': Card.objects.filter(~Q(pool='none')).order_by('name'),
        'slots': range(1, 5)
    }
    return render(request, 'snap/add.html', context)


@login_required
def add_card(request):
    card = Card(
        name = request.POST.get('name'),
        image = request.FILES['image'],
        cost = request.POST.get('cost'),
        power = request.POST.get('power'),
        description = request.POST.get('description'),
        pool = request.POST.get('pool'),
        released = True if request.POST.get('released') == 'on' else False,
        owned = True if request.POST.get('owned') == 'on' else False
    )
    card.save()
    return HttpResponseRedirect(reverse('snap:add'))


@login_required
def add_spotlight(request):
    if request.POST.get('card-4') != '':
        optional_card = Card.objects.get(name=request.POST.get('card-4'))
    else: optional_card = None
    spotlight = Spotlight.objects.create(
        date = request.POST.get('date'),
        card1 = Card.objects.get(name=request.POST.get('card-1')),
        card2 = Card.objects.get(name=request.POST.get('card-2')),
        card3 = Card.objects.get(name=request.POST.get('card-3')),
        card4 = optional_card,
        pulled1 = True if request.POST.get('pulled-1') == 'on' else False,
        pulled2 = True if request.POST.get('pulled-2') == 'on' else False,
        pulled3 = True if request.POST.get('pulled-3') == 'on' else False,
        pulled4 = True if request.POST.get('pulled-4') == 'on' else False
    )
    return HttpResponseRedirect(reverse('snap:add'))