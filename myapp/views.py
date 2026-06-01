from django.shortcuts import render
from django.http import HttpResponse
from .models import *   # นำเข้าโมเดล Member และ Product ที่เราสร้างไว้ใน models.py มาใช้งานใน views.py เพื่อให้สามารถดึงข้อมูลจากฐานข้อมูลมาแสดงผลในหน้าเว็บได้
from .forms import UserRegisterForm  # นำเข้า UserRegisterForm ที่เราสร้างไว้ใน forms.py มาใช้งานใน views.py เพื่อให้สามารถใช้ฟอร์มลงทะเบียนผู้ใช้ใหม่ในหน้าเว็บได้
from django.contrib import messages  # นำเข้า messages จาก django.contrib เพื่อใช้ในการแสดงข้อความแจ้งเตือนต่างๆ เช่น เมื่อผู้ใช้ลงทะเบียนสำเร็จ หรือเกิดข้อผิดพลาดในการกรอกข้อมูลในฟอร์มลงทะเบียน เป็นต้น
from django.shortcuts import redirect  # นำเข้า redirect จาก django.shortcuts เพื่อใช้ในการเปลี่ยนเส้นทางผู้ใช้ไปยังหน้าอื่นหลังจากที่ทำการลงทะเบียนสำเร็จ หรือเมื่อเกิดข้อผิดพลาดในการกรอกข้อมูลในฟอร์มลงทะเบียน เป็นต้น
from django.contrib.auth import authenticate, login as auth_login  # นำเข้า authenticate และ login จาก django.contrib.auth เพื่อใช้ในการยืนยันตัวตนและเข้าสู่ระบบ

def home(request):
    return render(request, 'home.html')   # localhost:8000/ -> home.html

def About(request):
    return render(request, 'about.html')  # localhost:8000/about -> about.html

def AllProducts(request):
    products = Product.objects.all()  # ดึงข้อมูลสินค้าทั้งหมดจากฐานข้อมูลมาเก็บไว้ในตัวแปร products
    context = {'products': products}  # สร้างตัวแปร context เพื่อเก็บข้อมูลสินค้าทั้งหมดที่เราดึงมาจากฐานข้อมูล เพื่อส่งไปยังเทมเพลต allproducts.html
    return render(request, 'allproducts.html', context)  # ส่งข้อมูลสินค้าทั้งหมดไปยังเทมเพลต allproducts.html เพื่อให้สามารถแสดงข้อมูลสินค้าในหน้าเว็บได้

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid(): 
            form.save() # บันทึกข้อมูลผู้ใช้ใหม่ลงในฐานข้อมูล โดยฟอร์ม UserRegisterForm ที่เราสร้างไว้ใน forms.py จะทำหน้าที่ตรวจสอบความถูกต้องของข้อมูลที่ผู้ใช้กรอกเข้ามา และเมื่อข้อมูลถูกต้องแล้วจะทำการบันทึกข้อมูลผู้ใช้ใหม่ลงในฐานข้อมูลโดยอัตโนมัติ
            username = form.cleaned_data.get('username') # ดึงข้อมูลชื่อผู้ใช้ที่ผู้ใช้กรอกเข้ามาในฟอร์มลงทะเบียน โดยใช้ cleaned_data ซึ่งเป็นพจนานุกรมที่เก็บข้อมูลที่ถูกต้องและผ่านการตรวจสอบแล้วจากฟอร์มลงทะเบียน และใช้ get() เพื่อดึงค่าของฟิลด์ username ออกมาเก็บไว้ในตัวแปร username
            messages.success(request, f'บัญชีผู้ใช้ {username} ถูกสร้างเรียบร้อยแล้ว! คุณสามารถเข้าสู่ระบบได้เลย')  # แสดงข้อความแจ้งเตือนเมื่อผู้ใช้ลงทะเบียนสำเร็จ
            return redirect('allproducts')  # เปลี่ยนเส้นทางผู้ใช้ไปยังหน้า allproducts หลังจากที่ทำการลงทะเบียนสำเร็จ
        
    else:
        form = UserRegisterForm()  # สร้างอินสแตนซ์ของฟอร์มลงทะเบียน UserRegisterForm เพื่อให้สามารถแสดงฟอร์มลงทะเบียนในหน้าเว็บได้  
    return render(request, 'register.html', {'form': form})  # ส่งข้อมูลฟอร์มลงทะเบียนไปยังเทมเพลต register.html เพื่อให้สามารถแสดงฟอร์มลงทะเบียนในหน้าเว็บได้    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # ดึงข้อมูลชื่อผู้ใช้จาก POST request
        password = request.POST.get('password')  # ดึงข้อมูลรหัสผ่านจาก POST request
        user = authenticate(request, username=username, password=password)  # ยืนยันตัวตนของผู้ใช้ โดยใช้ username และ password
        
        if user is not None:  # ถ้าผู้ใช้มีอยู่ในฐานข้อมูลและรหัสผ่านถูกต้อง
            auth_login(request, user)  # ทำการเข้าสู่ระบบ
            messages.success(request, f'ยินดีต้อนรับ {username}!')  # แสดงข้อความแจ้งเตือนเมื่อเข้าสู่ระบบสำเร็จ
            return redirect('allproducts')  # เปลี่ยนเส้นทางผู้ใช้ไปยังหน้า allproducts
        else:  # ถ้าชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')  # แสดงข้อความแจ้งเตือนเมื่อการเข้าสู่ระบบล้มเหลว
    
    return render(request, 'login.html')  # แสดงหน้า login

