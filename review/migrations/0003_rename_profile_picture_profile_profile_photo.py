# Generated by Django 4.0.5 on 2022-06-13 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='profile_photo',
        ),
    ]