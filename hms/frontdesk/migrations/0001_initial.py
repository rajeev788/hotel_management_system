# Generated by Django 4.2.7 on 2023-11-07 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('work', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='guest_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontdesk.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.room')),
            ],
        ),
    ]
