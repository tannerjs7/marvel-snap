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