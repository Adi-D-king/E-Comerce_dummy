# Generated by Django 5.0.7 on 2024-10-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_accounts_cart_id_address_carts'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='cart_id',
            field=models.IntegerField(default=None),
        ),
    ]
