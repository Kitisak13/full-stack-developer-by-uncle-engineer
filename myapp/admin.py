from django.contrib import admin
from .models import Member, Product, Profile  # นำเข้าโมเดล Member, Product และ Profile ที่เราสร้างไว้ใน models.py มาใช้งานใน admin.py เพื่อให้สามารถจัดการข้อมูลผ่านหน้าแอดมินได้

# Register your models here.
admin.site.register(Member) # ลงทะเบียนโมเดล Member กับแอดมิน เพื่อให้สามารถเพิ่ม แก้ไข ลบ ข้อมูลสมาชิกผ่านหน้าแอดมินได้

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'image', 'other')  # กำหนดฟิลด์ที่จะแสดงในหน้าแอดมินเมื่อดูรายการสินค้า โดยสามารถเลือกแสดงฟิลด์ที่ต้องการได้ตามต้องการ
    search_fields = ('title',) # เพิ่มฟีเจอร์การค้นหาข้อมูลสินค้าในหน้าแอดมิน โดยสามารถค้นหาจากชื่อสินค้า รายละเอียดสินค้า และข้อมูลอื่นๆ ได้

admin.site.register(Product, ProductAdmin) # ลงทะเบียนโมเดล Product กับแอดมิน และใช้ ProductAdmin เพื่อให้สามารถเพิ่ม แก้ไข ลบ ข้อมูลสินค้าผ่านหน้าแอดมินได้

admin.site.register(Profile) # ลงทะเบียนโมเดล Profile กับแอดมิน เพื่อให้สามารถเพิ่ม แก้ไข ลบ ข้อมูลโปรไฟล์ผ่านหน้าแอดมินได้