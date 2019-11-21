# Generated by Django 2.2 on 2019-11-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('place', models.CharField(max_length=255)),
                ('responsible', models.TextField()),
                ('level', models.CharField(max_length=200)),
                ('sport', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('docs', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
    ]
