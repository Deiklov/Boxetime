# Generated by Django 2.2.4 on 2020-02-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxetime', '0002_auto_20191225_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrequest',
            name='rank',
            field=models.CharField(blank=True, choices=[('novice', 'Новичок'), ('third', 'Третий разряд'), ('second', 'Второй разряд'), ('first', 'Первый разряд'), ('kms', 'КМС'), ('master', 'Мастер спорта')], default='novice', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='addrequest',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(60, '[0,60)'), (64, '[60;64)'), (69, '[64,69)'), (75, '[69,75)'), (81, '[75,81)'), (91, '[81,91)'), (500, '[91+)')], default=75, null=True),
        ),
    ]
