# Generated by Django 4.1.3 on 2022-12-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='bid_price',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='on_watchlist',
            field=models.BooleanField(default=False),
        ),
    ]
