# Generated by Django 3.2.7 on 2021-10-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=5)),
                ('standard', models.IntegerField()),
            ],
        ),
    ]