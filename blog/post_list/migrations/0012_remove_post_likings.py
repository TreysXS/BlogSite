# Generated by Django 3.2.4 on 2021-07-03 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_list', '0011_auto_20210704_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likings',
        ),
    ]