# Generated by Django 3.1.4 on 2021-05-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210506_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_network',
            name='coverage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
