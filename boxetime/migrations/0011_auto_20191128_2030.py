# Generated by Django 2.2 on 2019-11-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('boxetime', '0010_auto_20191128_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='competitid',
        ),
        migrations.AddField(
            model_name='competitgrid',
            name='competitid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='boxetime.Competition'),
        ),
    ]