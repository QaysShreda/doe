# Generated by Django 3.1.4 on 2021-05-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_network',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='coverage',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='port',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='switch',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
