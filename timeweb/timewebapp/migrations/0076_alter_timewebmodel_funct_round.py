# Generated by Django 3.2.7 on 2021-09-19 18:40

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timewebapp', '0075_alter_timewebmodel_funct_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timewebmodel',
            name='funct_round',
            field=models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), "This field's value must be positive")]),
        ),
    ]
