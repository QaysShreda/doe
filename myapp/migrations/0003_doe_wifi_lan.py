# Generated by Django 3.1.4 on 2021-04-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210424_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='doe_wifi',
            name='lan',
            field=models.CharField(max_length=50, null=True),
        ),
    ]