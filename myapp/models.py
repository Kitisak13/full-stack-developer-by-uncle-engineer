from django.db import models
from django.contrib.auth.models import User  # นำเข้าโมเดล User ที่มีอยู่ใน Django มาใช้งานใน models.py เพื่อสร้างโมเดล Profile ที่เชื่อมโยงกับโมเดล User ได้อย่างง่ายดาย โดยไม่ต้องสร้างฟิลด์สำหรับชื่อผู้ใช้ รหัสผ่าน และอีเมลด้วยตัวเอง เพราะโมเดล User มีฟิลด์เหล่านี้อยู่แล้ว และเราสามารถใช้ความสัมพันธ์ OneToOneField เพื่อเชื่อมโยงโมเดล Profile กับโมเดล User ได้อย่างสะดวกและมีประสิทธิภาพ
from django.dispatch import receiver # นำเข้า receiver จาก django.dispatch เพื่อใช้ในการสร้างสัญญาณ (signals) ที่จะทำงานเมื่อมีการบันทึกข้อมูลของโมเดล User ซึ่งจะช่วยให้เราสามารถสร้างโปรไฟล์อัตโนมัติสำหรับผู้ใช้ใหม่ได้โดยไม่ต้องเขียนโค้ดซ้ำซ้อนใน views.py หรือที่อื่นๆ ในโปรเจกต์ของเรา
from django.db.models.signals import post_save  # นำเข้า post_save signal จาก django.db.models.signals เพื่อใช้ในการสร้างสัญญาณที่จะทำงานเมื่อมีการบันทึกข้อมูลของโมเดล User

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    point = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True) # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True

    def __str__(self):
        return self.name   # เมื่อเราเรียกใช้ข้อมูลสมาชิกในรูปแบบของสตริง จะคืนค่าชื่อสมาชิกออกมาแทนที่จะเป็นตัวอ้างอิงของวัตถุ Member ในฐานข้อมูล
    #   return f"{self.name} - {self.tel} - {self.email} - {self.point} - {self.address}" # ถ้าอยากให้แสดงข้อมูลอื่นๆ ด้วย สามารถใช้ f-string เพื่อจัดรูปแบบการแสดงผลได้ตามต้องการ    


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='ชื่อสินค้า')  # verbose_name ใช้สำหรับกำหนดชื่อที่จะแสดงในหน้าแอดมินแทนชื่อฟิลด์
    detail = models.TextField(verbose_name='รายละเอียดสินค้า', null=True, blank=True)  # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True    
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='รูปสินค้า')  # upload_to กำหนดโฟลเดอร์ที่ใช้เก็บไฟล์รูปภาพที่อัพโหลดเข้ามาในระบบ ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True
    other = models.CharField(null=True, blank=True, verbose_name='อื่นๆ')  # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True

    def __str__(self):
        return self.title   # เมื่อเราเรียกใช้ข้อมูลสินค้าในรูปแบบของสตริง จะคืนค่าชื่อสินค้าออกมาแทนที่จะเป็นตัวอ้างอิงของวัตถุ Product ในฐานข้อมูล
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, null=True, blank=True, verbose_name='ชื่อ-นามสกุล')  # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='รูปโปรไฟล์')
    bio = models.TextField(null=True, blank=True, verbose_name='ข้อมูลส่วนตัว')  # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True
    website = models.URLField(null=True, blank=True, verbose_name='เว็บไซต์')  # ถ้าไม่บังคับกรอกให้ใส่ null=True, blank=True

    def __str__(self):
        return self.fullname   # เมื่อเราเรียกใช้ข้อมูลสมาชิกในรูปแบบของสตริง จะคืนค่าชื่อสมาชิกออกมาแทนที่จะเป็นตัวอ้างอิงของวัตถุ Profile ในฐานข้อมูล

@receiver(post_save, sender=User)  # ใช้สัญญาณ post_save เพื่อให้ฟังก์ชัน create_user_profile ถูกเรียกใช้งานทุกครั้งที่มีการบันทึกข้อมูลของโมเดล User ไม่ว่าจะเป็นการสร้างผู้ใช้ใหม่หรือการแก้ไขข้อมูลผู้ใช้ที่มีอยู่แล้ว
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # ตรวจสอบว่าเป็นการสร้างผู้ใช้ใหม่หรือไม่ ถ้าเป็นการสร้างผู้ใช้ใหม่จะมีค่า created เป็น True และจะทำการสร้างโปรไฟล์ใหม่ให้กับผู้ใช้คนนั้นโดยอัตโนมัติ
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # ใช้สัญญาณ post_save เพื่อให้ฟังก์ชัน save_user_profile ถูกเรียกใช้งานทุกครั้งที่มีการบันทึกข้อมูลของโมเดล User ไม่ว่าจะเป็นการสร้างผู้ใช้ใหม่หรือการแก้ไขข้อมูลผู้ใช้ที่มีอยู่แล้ว
def save_user_profile(sender, instance, **kwargs): # ฟังก์ชันนี้จะทำงานเมื่อมีการบันทึกข้อมูลของโมเดล User ไม่ว่าจะเป็นการสร้างผู้ใช้ใหม่หรือการแก้ไขข้อมูลผู้ใช้ที่มีอยู่แล้ว โดยจะทำการบันทึกข้อมูลของโปรไฟล์ที่เชื่อมโยงกับผู้ใช้คนนั้นด้วย เพื่อให้แน่ใจว่าข้อมูลโปรไฟล์จะถูกอัพเดตทุกครั้งที่มีการเปลี่ยนแปลงข้อมูลของผู้ใช้
    instance.profile.save() # บันทึกข้อมูลของโปรไฟล์ที่เชื่อมโยงกับผู้ใช้คนนั้นด้วย เพื่อให้แน่ใจว่าข้อมูลโปรไฟล์จะถูกอัพเดตทุกครั้งที่มีการเปลี่ยนแปลงข้อมูลของผู้ใช้