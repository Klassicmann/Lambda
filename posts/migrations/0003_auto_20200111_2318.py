# Generated by Django 2.2 on 2020-01-11 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200111_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='add description'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=250),
        ),
    ]