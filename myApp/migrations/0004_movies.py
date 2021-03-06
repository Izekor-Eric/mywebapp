# Generated by Django 3.1.2 on 2020-11-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0003_delete_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=10, unique=True)),
                ('movie_type', models.CharField(max_length=10)),
                ('released_country', models.CharField(max_length=10)),
                ('movies_characters', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=10)),
                ('released_date', models.CharField(max_length=10)),
            ],
        ),
    ]
