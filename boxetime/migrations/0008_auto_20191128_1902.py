# Generated by Django 2.2 on 2019-11-28 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boxetime', '0007_auto_20191128_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrequest',
            name='role',
            field=models.CharField(
                choices=[('Doctor', 'Врач'), ('Participant', 'Участник'), ('Coach', 'Тренер'), ('Sponsor', 'Cпонсор')],
                default='Participant', max_length=100),
        ),
        migrations.AlterField(
            model_name='competition',
            name='sport',
            field=models.CharField(choices=[('Boxing', 'Бокс'), ('Kickboxing', 'Кикбоксинг')], default='Boxing',
                                   max_length=50),
        ),
        migrations.CreateModel(
            name='CompetitGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winuser', models.PositiveSmallIntegerField(blank=True, choices=[(models.ForeignKey(null=True,
                                                                                                     on_delete=django.db.models.deletion.SET_NULL,
                                                                                                     related_name='member1',
                                                                                                     to=settings.AUTH_USER_MODEL),
                                                                                   'member1'), (
                                                                                  models.ForeignKey(null=True,
                                                                                                    on_delete=django.db.models.deletion.SET_NULL,
                                                                                                    related_name='member2',
                                                                                                    to=settings.AUTH_USER_MODEL),
                                                                                  'member2')])),
                ('weight', models.PositiveSmallIntegerField(blank=True)),
                ('levelgrid', models.PositiveSmallIntegerField(blank=True)),
                ('competitid',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='boxetime.Competition')),
                ('member1',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member1',
                                   to=settings.AUTH_USER_MODEL)),
                ('member2',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member2',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]