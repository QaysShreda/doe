from django.db import models

# Create your models here.
class Doe_computer(models.Model):
    ram_type_list = [
        ('DDR2','DDR2'),
        ('DDR3','DDR3'),
        ('DDR4','DDR4'),
        ('Other','Other')
    ]
    hdd_list=[
        ('SATA','SATA'),
        ('SSD','SSD'),
        ('Other','Other')
    ]
    employee_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    ram_type = models.CharField(choices=ram_type_list,max_length=50)
    hdd = models.CharField(max_length=50)
    hdd_type = models.CharField(choices=hdd_list,max_length=50)
    ip = models.CharField(max_length=50)
    monitor = models.CharField(max_length=50)
    serial = models.CharField(max_length=50,blank=True)
    anti_viruse = models.CharField(max_length=50)
    expiry_date = models.DateField()

class Doe_copier(models.Model):
    brand_name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    place = models.CharField(max_length=150)
    company = models.CharField(max_length=50)
    company_phone = models.CharField(max_length=50)
    driver = models.CharField(max_length=100)

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

class Doe_Fiber(models.Model):
    location = models.CharField(max_length=50)
    line_code = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    support = models.CharField(max_length=50)

class Doe_Wifi(models.Model):
    router = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    lan = models.CharField(max_length=50, null=True)
    ssid = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50)

class Common_Ip(models.Model):
    department = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    port = models.CharField(max_length=50)


class School(models.Model):
    school_level=[
        ('1','الاول الاساسي'),
        ('2', 'الثاني الاساسي'),
        ('3', 'الثالث الاساسي'),
        ('4', 'الرابع الاساسي'),
        ('5', 'الخامس الاساسي'),
        ('6', ' السادس الاساسي'),
        ('7', 'السابع الاساسي'),
        ('8', 'الثامن الاساسي'),
        ('9', 'التاسع الاساسي'),
        ('10', 'العاشر الاساسي'),
        ('11', 'الحادي عشر'),
        ('12', 'الثاني عشر'),
    ]
    school_type=[
        ('ذكور','ذكور'),
        ('إناث','إناث'),
        ('مختلط','مختلط')
    ]
    area_type=[
        ('A','منطقة أ'),
        ('B','منطقة ب'),
        ('C','منطقة ج')
    ]
    school_id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    l_level = models.CharField(choices=school_level,max_length=50)
    u_level = models.CharField(choices=school_level,max_length=50)
    type= models.CharField(choices=school_type,max_length=50)
    st_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    region= models.CharField(choices=area_type,max_length=50,default='منطقة أ')
    mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class School_lab(models.Model):
    network = models.BooleanField(default=False)
    area = models.IntegerField()
    internet_connection = models.BooleanField(default=False)
    teacher = models.CharField(max_length=50)
    teacher_load = models.CharField(max_length=20)
    projector = models.BooleanField(default=False)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class School_computer(models.Model):
    brand = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    hdd = models.CharField(max_length=20)
    internet = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    serial = models.CharField(max_length=50,blank=True)
    lab = models.ForeignKey(School_lab,on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)












