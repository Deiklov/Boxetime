# Generated by Django 2.2.4 on 2019-12-24 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.png', upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('place', models.CharField(max_length=255)),
                ('responsible', models.TextField(blank=True)),
                ('level', models.CharField(max_length=200)),
                ('sport', models.CharField(choices=[('Boxing', 'Бокс'), ('Kickboxing', 'Кикбоксинг')], default='Boxing',
                                           max_length=50)),
                ('description', models.TextField(blank=True)),
                ('docs', models.FileField(blank=True, null=True, upload_to='docs/')),
                ('author', models.ForeignKey(default=1, on_delete=models.SET(1), to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(blank=True)),
                ('levelgrid', models.PositiveSmallIntegerField(blank=True)),
                ('competitid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boxetime.Competition')),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member1', to=settings.AUTH_USER_MODEL)),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member2', to=settings.AUTH_USER_MODEL)),
                ('memberwin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memberwin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Doctor', 'Врач'), ('Participant', 'Участник'), ('Coach', 'Тренер'),
                                                   ('Sponsor', 'Cпонсор')], default='Participant', max_length=100)),
                ('weight', models.PositiveSmallIntegerField()),
                ('docs', models.FileField(blank=True, upload_to='docs/')),
                ('acepted', models.BooleanField(default=False)),
                ('rank', models.CharField(
                    choices=[('novice', 'Новичок'), ('third', 'Третий разряд'), ('second', 'Второй разряд'),
                             ('first', 'Первый разряд'), ('kms', 'КМС'), ('master', 'Мастер спорта')], default='novice',
                    max_length=50)),
                ('competit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxetime.Competition')),
                ('userid', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
