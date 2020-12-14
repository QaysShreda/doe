# Generated by Django 3.1.4 on 2020-12-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_doe_copier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doe_printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=50)),
                ('Cartege_number', models.CharField(max_length=50)),
                ('driver', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='doe_computer',
            old_name='barnd_name',
            new_name='brand_name',
        ),
    ]
