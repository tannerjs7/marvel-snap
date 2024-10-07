# Generated by Django 5.1.1 on 2024-10-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='pool',
            field=models.CharField(choices=[('Starter', 'Starter Card'), ('Recruit', 'Recruit Season'), ('1', 'Pool 1'), ('2', 'Pool 2'), ('3', 'Pool 3'), ('4', 'Pool 4'), ('5', 'Pool 5'), ('None', 'None')], default='None', max_length=20),
        ),
    ]
