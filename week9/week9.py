print("تكليفات الدروس من الدرس 065 إلى 068")
print("-" * 50)
print("Assignment 1")

import os

# إنشاء مجلد Python على سطح المكتب
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
python_folder_path = os.path.join(desktop_path, "Python")
os.makedirs(python_folder_path, exist_ok=True)

# إنشاء ملف assign.py داخل المجلد Python
assign_file_path = os.path.join(python_folder_path, "assign.py")
with open(assign_file_path, 'w') as assign_file:
    pass  # لا يوجد محتوى في هذا الملف حاليا

# إنشاء 50 ملف نصي داخل المجلد Python
for i in range(1, 51):
    txt_file_path = os.path.join(python_folder_path, f"txt{i}.txt")
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write(f"Elzero Web School => {i}")

    # تسمية الملف رقم 25 ب special-text
    if i == 25:
        os.rename(txt_file_path, os.path.join(python_folder_path, "special-text.txt"))

# فتح الملف special-text.txt
with open(os.path.join(python_folder_path, "special-text.txt"), 'a') as special_text_file:
    pass  # الملف سيظل فارغا

# طباعة معلومات إضافية
print("Current Working Directory:", os.getcwd())
print("Current File Path:", os.path.abspath(assign_file_path))
print("Current Opened File:", assign_file_path.split(os.path.sep)[-1])

# طباعة عدد الملفات في المجلد Python
file_count = len([f for f in os.listdir(python_folder_path) if os.path.isfile(os.path.join(python_folder_path, f))])
print("Total Files in Python Folder:", file_count)


print("-" * 50)
print("Assignment 2 ")

# فتح الملف txt1.txt
txt1_file_path = os.path.join(python_folder_path, "txt1.txt")
with open(txt1_file_path, 'a') as txt1_file:
    # السطر الأول لا يتغير
    txt1_file.write("Elzero Web School => 1\n")

    # كتابة Appended => Elzero Web School خمسون مرة
    for i in range(50):
        txt1_file.write(f"Appended => Elzero Web School\n")



print("-" * 50)
print("Assignment 2 ")

# فتح الملف txt1.txt للقراءة
with open(txt1_file_path, 'r') as txt1_file:
    # قراءة جميع الأسطر
    lines = txt1_file.readlines()

    # طباعة عدد الأسطر
    print("Number of Lines in txt1.txt:", len(lines))

    # حساب عدد الكلمات
    words_count = sum(len(line.split()) for line in lines)
    print("Number of Words in txt1.txt:", words_count)

    # حساب عدد الحروف
    characters_count = sum(len(line) for line in lines)
    print("Number of Characters in txt1.txt:", characters_count)

    # حساب عدد مرات وجود الحرف "l"
    l_count = sum(line.count('l') for line in lines)
    print("Number of 'l' occurrences in txt1.txt:", l_count)
