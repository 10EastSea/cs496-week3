# Generated by Django 3.1.5 on 2021-01-18 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='userName',
            new_name='userID',
        ),
    ]