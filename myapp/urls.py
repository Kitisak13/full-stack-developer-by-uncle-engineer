from django.urls import path
from .views import home, About, AllProducts, register, login  # นำเข้า view ที่เราสร้างไว้ใน myapp/views.py ดึงมาเฉพาะฟังก

urlpatterns = [
    path('',home), # กำหนด URL pattern สำหรับหน้า homepage โดยใช้ฟังก์ชัน home ที่เรานำเข้า
    path('about', About),
    path('allproducts', AllProducts),
    path('register', register, name='register'),  # กำหนด URL pattern สำหรับหน้า register โดยใช้ฟังก์ชัน register ที่เรานำเข้า และตั้งชื่อ pattern เป็น 'register'
    path('login', login, name='login'),  # กำหนด URL pattern สำหรับหน้า login โดยใช้ฟังก์ชัน login ที่เรานำเข้า และตั้งชื่อ pattern เป็น 'login'
]