# Generated by Django 3.1.4 on 2021-05-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210506_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_network',
            name='brand',
            field=models.CharField(blank=True, default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school_network',
            name='coverage',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='port',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='speed_download',
            field=models.IntegerField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='speed_upload',
            field=models.IntegerField(blank=True, default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='school_network',
            name='switch',
            field=models.CharField(blank=True, default=0, max_length=50),
            preserve_default=False,
        ),
    ]