# Generated by Django 3.2.12 on 2022-05-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipmodels',
            name='membership',
            field=models.CharField(choices=[('1', 'basic'), ('2', 'premium'), ('3', 'enterprice'), ('4', 'custom')], default='basic', max_length=16),
        ),
    ]
