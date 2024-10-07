from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Card


def index(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request, 'snap/index.html', context)


# add try/except/else
def toggle_owned(request, card_name):
    card = get_object_or_404(Card, pk=card_name)
    if request.POST.get('owned') == 'on': card.owned = True
    else: card.owned = False
    card.save()
    return HttpResponseRedirect(reverse('snap:index'))