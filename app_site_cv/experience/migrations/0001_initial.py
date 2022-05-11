# Generated by Django 4.0.4 on 2022-05-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperiencePro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metier', models.CharField(max_length=150)),
                ('societe', models.CharField(max_length=150)),
                ('contenu', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]