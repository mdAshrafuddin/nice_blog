# Generated by Django 3.1.4 on 2021-02-07 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='next_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_post',
        ),
    ]
