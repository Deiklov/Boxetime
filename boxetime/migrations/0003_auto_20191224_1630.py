# Generated by Django 2.2.4 on 2019-12-24 13:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boxetime', '0002_remove_profile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='author',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='competition',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
