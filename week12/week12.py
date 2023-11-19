print('#' * 50)
print("تكليفات الدروس من الدرس 086 إلى 089")
print("#" * 50)

print("التكليف 01")

my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

final_string = ''

for data in zip(my_list, my_tuple):
    my_data = data[0] + data[1]
    final_string += my_data

final_string = final_string.capitalize()

print(final_string)  # Elzero

# ---------------------------------------------------------------------
print("#" * 50)
print("التكليف 02")

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    my_data += str(item1)

final = "".join(my_data[0:-2]).capitalize()

print(final)

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     # Write Your Code Here
#     my_data = (my_list1[0:-2])
#
# finial = ''.join(my_data).capitalize()
#
# print(finial)

# ---------------------------------------------------------------------
print("#" * 50)
print("التكليف 03")

# لديك الصورة التالية حجمها 1200 العرض في 800 الطول
# 2 rows 3 col
# each image = 400 * 400
# 1200 / 3 = 400
# 800 / 2 = 400

# from PIL import Image
#
# my_image = Image.open("elzero-pillow.png")
#
# my_image.show()
#
# # cutting the image (left, upper, right, lower)
# my_box = (400, 0, 800, 400)
# my_new_image = my_image.crop(my_box)
# my_new_image = my_new_image.convert("L")
#
# my_new_image.show()
#
# # -----------------------------------------------------
#
# my_image = Image.open("elzero-pillow.png")
# # my_image.show()
#
# my_box = (0, 400, 1200, 800)
# my_new_image2 = my_image.crop(my_box)
# my_new_image2 = my_new_image2.convert("L")
# # my_new_image.show()
#
# rotated_image = my_new_image2.rotate(180)
# rotated_image.show()

# ---------------------------------------------------------------------
print("#" * 50)
print("التكليف 04")


# Write Function With Help To Get The Output
def say_hello_to(name):
    """
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"
    """
    return f"Hello {name}"


print(say_hello_to("Osama"))  # "Hello Osama"

# Write Doc String Line For The Function Here
print(say_hello_to.__doc__)

# Function Doc String Output
# "parameter(someone) => Person Name"
# "Function To Say Hello To Anyone"

# ---------------------------------------------------------------------
print("#" * 50)
print("التكليف 04")

my_friends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_people) -> list:
    """DOC STRING FOUND"""
    for some_one in some_people:
        print(f"Hello {some_one}")


say_hello(my_friends)

# pylint.exe D:\_Learning\Python\PyCharm\Assignments\week12\week12.py
