# Generated by Django 3.2.3 on 2021-09-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_alter_analytics_request_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='date_parsed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
