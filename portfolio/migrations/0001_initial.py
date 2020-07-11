# Generated by Django 3.0.8 on 2020-07-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
