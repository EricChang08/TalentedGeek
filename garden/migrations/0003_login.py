# Generated by Django 3.0.6 on 2020-08-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_auto_20200627_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr', models.CharField(default='', max_length=100000)),
                ('psw', models.CharField(default='', max_length=100000)),
            ],
        ),
    ]