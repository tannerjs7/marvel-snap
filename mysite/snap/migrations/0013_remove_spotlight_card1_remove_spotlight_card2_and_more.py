# Generated by Django 5.1.1 on 2024-11-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0012_spotlight_cards_alter_spotlight_card1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotlight',
            name='card1',
        ),
        migrations.RemoveField(
            model_name='spotlight',
            name='card2',
        ),
        migrations.RemoveField(
            model_name='spotlight',
            name='card3',
        ),
        migrations.RemoveField(
            model_name='spotlight',
            name='card4',
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='cards',
            field=models.ManyToManyField(blank=True, related_name='spotlights', to='snap.card'),
        ),
    ]