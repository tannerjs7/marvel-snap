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