# Generated by Django 5.1.1 on 2024-12-04 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0014_remove_spotlight_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotlight',
            name='card1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spotlights1', to='snap.card'),
        ),
        migrations.AddField(
            model_name='spotlight',
            name='card2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spotlights2', to='snap.card'),
        ),
        migrations.AddField(
            model_name='spotlight',
            name='card3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spotlights3', to='snap.card'),
        ),
        migrations.AddField(
            model_name='spotlight',
            name='card4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spotlights4', to='snap.card'),
        ),
    ]