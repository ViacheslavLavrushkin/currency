# Generated by Django 3.2.3 on 2021-08-14 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code_name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField()),
                ('original_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=120)),
                ('email_from', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Dollar'), (1, 'Euro')])),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('counter', models.PositiveBigIntegerField()),
                ('request_method', models.PositiveSmallIntegerField(choices=[(0, 'GET'), (1, 'POST')])),
                ('status_code', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('path', 'request_method', 'status_code')},
            },
        ),
    ]
