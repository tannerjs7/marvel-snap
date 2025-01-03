# Generated by Django 5.1.1 on 2024-11-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0011_remove_spotlight_cards_spotlight_card1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlight',
            name='cards',
            field=models.ManyToManyField(related_name='spotlights', to='snap.card'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='card1',
            field=models.CharField(default=None, max_length=50, verbose_name='Card 1'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='card2',
            field=models.CharField(default=None, max_length=50, verbose_name='Card 2'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='card3',
            field=models.CharField(default=None, max_length=50, verbose_name='Card 3'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='card4',
            field=models.CharField(default=None, max_length=50, verbose_name='Card 4'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='pulled1',
            field=models.BooleanField(default=False, verbose_name='Pulled Card 1'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='pulled2',
            field=models.BooleanField(default=False, verbose_name='Pulled Card 2'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='pulled3',
            field=models.BooleanField(default=False, verbose_name='Pulled Card 3'),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='pulled4',
            field=models.BooleanField(default=False, verbose_name='Pulled Card 4'),
        ),
    ]
