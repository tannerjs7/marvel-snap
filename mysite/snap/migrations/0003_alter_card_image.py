# Generated by Django 5.1.1 on 2024-10-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0002_card_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
