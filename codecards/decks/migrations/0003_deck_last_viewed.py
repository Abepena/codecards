# Generated by Django 2.1 on 2018-08-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_auto_20180818_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='last_viewed',
            field=models.DateField(auto_now=True),
        ),
    ]
