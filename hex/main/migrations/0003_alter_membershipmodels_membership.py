# Generated by Django 3.2.12 on 2022-05-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_membershipmodels_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipmodels',
            name='membership',
            field=models.CharField(choices=[('basic', 'basic'), ('premium', 'premium'), ('enterprice', 'enterprice'), ('custom', 'custom')], default='basic', max_length=16),
        ),
    ]
