# Generated by Django 4.0.5 on 2022-06-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(max_length=500),
        ),
    ]
