# Generated by Django 2.2.4 on 2020-02-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxetime', '0003_auto_20200204_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateField(),
        ),
    ]
