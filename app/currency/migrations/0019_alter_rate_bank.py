# Generated by Django 3.2.3 on 2021-08-14 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0018_auto_20210814_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.bank'),
        ),
    ]
