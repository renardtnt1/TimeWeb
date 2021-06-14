# Generated by Django 3.1.8 on 2021-04-10 08:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('timewebapp', '0009_auto_20210409_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmodel',
            name='def_nwd',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('0', 'Sunday')], max_length=13, null=True, verbose_name="Default Weekdays you won't work"),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='show_progress_bar',
            field=models.BooleanField(default=True, verbose_name='Show Graph Progress Bar'),
        ),
    ]
