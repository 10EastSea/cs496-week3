# Generated by Django 3.1.5 on 2021-01-15 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mbti',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='userPW',
            field=models.TextField(),
        ),
    ]