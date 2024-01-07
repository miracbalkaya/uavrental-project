# Generated by Django 5.0.1 on 2024-01-07 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='renting_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.user'),
        ),
    ]