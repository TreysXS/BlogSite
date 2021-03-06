# Generated by Django 3.2.4 on 2021-07-03 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_list', '0010_auto_20210703_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post_list.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likings',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
