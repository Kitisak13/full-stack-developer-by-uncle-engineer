# Django Project - การแก้ไขข้อผิดพลาด

## สรุปข้อผิดพลาดที่เกิดขึ้น

เมื่อเพิ่ม `ImageField` ในโมเดล `Product` ปัญหาหลายอย่างเกิดขึ้น:

### 1. ❌ ข้อผิดพลาด: Pillow Library ไม่ได้ติดตั้ง
**Error Message:**
```
myapp.Product.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```

**สาเหตุ:**
- Django's `ImageField` ต้องใช้ **Pillow library** เพื่อจัดการและประมวลผลไฟล์รูปภาพ
- Pillow ยังไม่ได้ติดตั้งในสภาพแวดล้อม (environment)

**วิธีแก้ไข:**
```bash
pip install Pillow
```

---

### 2. ❌ ข้อผิดพลาด: Import Errors ใน VS Code
**Error Message:**
```
Import "django.db" could not be resolved from source
Import "django.shortcuts" could not be resolved from source
Import "django.contrib" could not be resolved from source
```

**สาเหตุ:**
- VS Code's Python Language Server (Pylance) ไม่สามารถหา Django packages ได้
- เนื่องจาก VS Code ใช้ Python environment ที่ไม่มี Django ติดตั้ง

**วิธีแก้ไข:**
1. ติดตั้ง Django ในสภาพแวดล้อม:
```bash
pip install Django
```

2. Reload VS Code Window:
   - กด `Ctrl + Shift + P`
   - พิมพ์ "Reload Window" 
   - กด Enter
   - นี่จะให้ Pylance อ่านแพ็คเกจใหม่

---

### 3. ⚠️ ปัญหา: Virtual Environments หลายตัว
**สถานการณ์:**
- โปรเจกต์มี **2 virtual environments**:
  - `.venv` - ที่ VS Code ใช้
  - `venv` - ที่ terminal ใช้

**วิธีแก้ไข:**
ต้องแน่ใจว่าติดตั้งแพ็คเกจในสภาพแวดล้อมที่ถูกต้อง (ที่ terminal ใช้):
```bash
# ตรวจสอบว่า venv ถูก activate แล้ว (ดูจากชื่อ (venv) ที่ด้านหน้า prompt)
pip install Pillow
pip install Django
```

---

## สรุปการแก้ไข

| ปัญหา | วิธีแก้ | สถานะ |
|-------|--------|------|
| Pillow ไม่ได้ติดตั้ง | `pip install Pillow` | ✅ แก้ไขแล้ว |
| Django ไม่ได้ติดตั้ง | `pip install Django` | ✅ แก้ไขแล้ว |
| Import errors ใน VS Code | Reload Window + ติดตั้ง Django | ✅ แก้ไขแล้ว |
| Virtual env หลายตัว | ใช้ venv ที่ terminal เปิดใช้งาน | ✅ ยืนยันแล้ว |

---

## บทเรียน

1. **ImageField ต้องการ Pillow**: ถ้าใช้ `ImageField` ใน Django model ต้องติดตั้ง Pillow
2. **ตรวจสอบ Python Environment**: ระบบและ IDE ต้องใช้ environment เดียวกัน
3. **Install Dependencies**: ติดตั้ง dependencies ทั้งหมดที่โปรเจกต์ต้องใช้

---

## Packages ที่ติดตั้ง

```
Django==5.2.8
Pillow==12.0.0
```

ตรวจสอบการติดตั้งได้โดยใช้:
```bash
pip list
```
