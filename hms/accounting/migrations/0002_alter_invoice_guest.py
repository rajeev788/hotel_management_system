# Generated by Django 4.2.7 on 2023-11-08 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0001_initial'),
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='guest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontdesk.guest'),
        ),
    ]
