# Generated by Django 2.2 on 2020-03-22 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0027_school_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=150, null=True)),
                ('account_type', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Bookseller', 'Bookseller')], max_length=20)),
                ('image', imagekit.models.fields.ProcessedImageField(default='default.png', upload_to='users/profile_images')),
                ('quater', models.CharField(blank=True, max_length=250, null=True)),
                ('town', models.CharField(blank=True, max_length=250, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('subscribers', models.IntegerField(default=0)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
