# Generated by Django 5.1.1 on 2024-10-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0007_alter_card_image_alter_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='pool',
            field=models.CharField(choices=[('starter', 'Starter Card'), ('recruit', 'Recruit Season'), ('1', 'Pool 1'), ('2', 'Pool 2'), ('3', 'Pool 3'), ('4', 'Pool 4'), ('5', 'Pool 5'), ('none', 'None')], default='None', max_length=20),
        ),
    ]
