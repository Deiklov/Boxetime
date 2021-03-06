# Generated by Django 2.2.4 on 2019-12-25 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('boxetime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrequest',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addrequest',
            name='weight',
            field=models.PositiveSmallIntegerField(
                choices=[(60, '[0,60)'), (64, '[60;64)'), (69, '[64,69)'), (75, '[69,75)'), (81, '[75,81)'),
                         (91, '[81,91)'), (500, '[91+)')]),
        ),
    ]
