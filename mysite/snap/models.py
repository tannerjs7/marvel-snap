from django.db import models


class Card(models.Model):
    POOL_CHOICES = {
        'starter': 'Starter Card',
        'recruit': 'Recruit Season',
        '1': 'Pool 1',
        '2': 'Pool 2',
        '3': 'Pool 3',
        '4': 'Pool 4',
        '5': 'Pool 5',
        'none': 'None'
    }

    name = models.CharField(primary_key=True, unique=True, max_length=50)
    image = models.ImageField(upload_to='card_images/')
    cost = models.IntegerField()
    power = models.IntegerField()
    description = models.CharField(max_length=300)
    pool = models.CharField(max_length=20, choices=POOL_CHOICES, default='None')
    owned = models.BooleanField(default=False)
    released = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Spotlight(models.Model):
    date = models.DateField()
    card1 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='first_spotlight_slots')
    card2 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='second_spotlight_slots')
    card3 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='third_spotlight_slots')
    card4 = models.ForeignKey(Card, blank=True, null=True, on_delete=models.SET_NULL, related_name='fourth_spotlights_slots')
    pulled1 = models.BooleanField(default=False, verbose_name='Pulled Card 1')
    pulled2 = models.BooleanField(default=False, verbose_name='Pulled Card 2')
    pulled3 = models.BooleanField(default=False, verbose_name='Pulled Card 3')
    pulled4 = models.BooleanField(default=False, verbose_name='Pulled Card 4')

    def __str__(self):
        return 'Spotlight ' + str(self.date)
    

class Deck(models.Model):
    name = models.CharField(max_length=100)
    card1 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='first_deck_slots')
    card2 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='second_deck_slots')
    card3 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='third_deck_slots')
    card4 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='fourth_deck_slots')
    card5 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='fifth_deck_slots')
    card6 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='sixth_deck_slots')
    card7 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='seventh_deck_slots')
    card8 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='eighth_deck_slots')
    card9 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='ninth_deck_slots')
    card10 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='tenth_deck_slots')
    card11 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='eleventh_deck_slots')
    card12 = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='twelfth_deck_slots')

    def __str__(self):
        return self.name
    

class Pack(models.Model):
    PACK_TYPE_CHOICES = {
        "seasonal_series_5": "Seasonal Series 5",
        "seasonal_series_4": "Seasonal Series 4",
        "collectors_series_5": "Collector's Series 5",
        "collectors_series_4": "Collector's Series 4",
        "collectors_series_3": "Collector's Series 3"
    }
        
    BONUS_CHOICES = {
        'card': 'Card',
        '25_tokens': '25 Tokens',
        '50_tokens': '50 Tokens',
        '100_tokens': '100 Tokens',
        '1000_tokens': '1000 Tokens',
        '15_boosters': '15 Boosters',
        '35_boosters': '35 Boosters',
        '65_boosters': '65 Boosters',
        '155_boosters': '155 Boosters',
        '50_credits': '50 Credits',
        '100_credits': '100 Credits',
        '200_credits': '200 Credits',
        '1525_credits': '1525 Credits',
        'border': 'Border',
        'variant': 'Variant'
    }

    pack_type = models.CharField(max_length=30, choices=PACK_TYPE_CHOICES, default='None')
    date = models.DateField()
    main_card = models.ForeignKey(Card, null=True, on_delete=models.SET_NULL, related_name='first_pack_slots')
    bonus_card1 = models.ForeignKey(Card, blank=True, null=True, on_delete=models.SET_NULL, related_name='second_pack_slots')
    bonus_card2 = models.ForeignKey(Card, blank=True, null=True, on_delete=models.SET_NULL, related_name='third_pack_slots')
    bonus1 = models.CharField(max_length=20, choices=BONUS_CHOICES, default='None')
    bonus2 = models.CharField(max_length=20, choices=BONUS_CHOICES, default='None')