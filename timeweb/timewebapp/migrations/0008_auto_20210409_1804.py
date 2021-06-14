# Generated by Django 3.1.8 on 2021-04-10 01:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timewebapp', '0007_auto_20210409_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmodel',
            name='warning_acceptance',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(1, "This field's value must be an integer from 1 to 100"), django.core.validators.MaxValueValidator(100, "This field's value must be an integer from 1 to 100")], verbose_name='Warning Threshold in Percent'),
        ),
        migrations.AlterField(
            model_name='timewebmodel',
            name='ctime',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), "This field's value must be positive")]),
        ),
        migrations.AlterField(
            model_name='timewebmodel',
            name='funct_round',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'), "This field's value must be positive")]),
        ),
        migrations.AlterField(
            model_name='timewebmodel',
            name='y',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(1, "This field's value cannot be less than %(limit_value)s")]),
        ),
    ]
