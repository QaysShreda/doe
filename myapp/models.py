from django.db import models

# Create your models here.
class Doe_computer(models.Model):
    employee_name = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    hdd = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    monitor = models.CharField(max_length=50)

class Doe_copier(models.Model):
    brand_name = models.CharField(max_length=50)
    copier_ip = models.CharField(max_length=50)
    copier_place = models.CharField(max_length=150)
    copier_company = models.CharField(max_length=50)
    copier_company_phone = models.CharField(max_length=50)
    copier_driver = models.CharField(max_length=100)

class Doe_printer(models.Model):
    model_name = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    Cartridge_number = models.CharField(max_length=50)
    driver = models.CharField(max_length=100)

class Doe_projector(models.Model):
    model_name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    warranty = models.CharField(max_length=50)






