# Generated by Django 5.1.1 on 2024-11-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0009_spotlight_card_spotlights'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='spotlights',
        ),
        migrations.AddField(
            model_name='spotlight',
            name='cards',
            field=models.ManyToManyField(related_name='spotlights', to='snap.card'),
        ),
    ]
