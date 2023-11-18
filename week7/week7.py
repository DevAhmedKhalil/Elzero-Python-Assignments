# print("#" * 50)
# print('تكليفات الدروس من الدرس 051 إلى 055')
# print("#" * 50)
#
# # 01 assignment
# # Needed Output
# # "1 => 20"
# # "2 => 15"
# # "3 => 5"
# # "All Numbers Printed"
#
# # Input
# my_nums = [15, 81, 5, 17, 20, 21, 13]
#
# # Use [For]
# n = 1
# my_nums.sort(reverse=True)
# for nums in my_nums:
#     if nums % 5 == 0:
#         print(f"{n} => {nums}")
#         n += 1
# else:
#     print("All nums printed!")
# # ------------------------------------------
# print("-" * 50)
# # Use [while]
# n = 1
# index = 0
# while len(my_nums) > index:
#     if my_nums[index] % 5 == 0:
#         print(f"{n} => {my_nums[index]}")
#         n += 1
#     index += 1
# else:
#     print("All nums printed!")
#
# # ------------------------------------------
# print("=" * 50)
# # ------------------------------------------
#
# # 02
# # Needed Output
# # قم بعمل Loop يطبع الأرقام من 1 إلى 20
# # إذا كان الرقم أقل من 10 ضع قبله صفر
# # قم بإستثناء الأرقام 6 و 8 و 12
# # قم بطباعة رسالة تفيد إنتهاء ال Loop بنجاح
#
# # start = 1
# # while start <= 20:
# #     if start not in [6, 8, 12]:
# #         print(str(start).zfill(2))
# #     start += 1
#
# start = 1
# while start <= 20:
#     if start == 6 or start == 8 or start == 12:
#         start += 1
#         continue
#     print(str(start).zfill(2))
#     start += 1
# else:
#     print("تم انتهاء الحلقة بنجاح!")
#
# # ------------------------------------------
# print("=" * 50)
# # ------------------------------------------
#
# # 03
# # لديك قاموس يحتوي على المواد العلمية الخاصة بك وال Rank الذي حصلت عليه
# # كل قيمة من القيم في ال Rank تساوي نقاط معينة
# # ال A تساوي 100 وال B تساوي 80 وال C تساوي 40
# # قم بإستخدام ما تعلمته سابقا لتخرج بالنتيجة التالية بدون التعديل على القاموس الأصلي
# # قم بطباعة مجموع النقاط في النهاية بعد إنتهاء ال Loop
# # -------------
# # Needed Output
# # "My Rank in Math Is A And This Equal 100 Points"
# # "My Rank in Science Is B And This Equal 80 Points"
# # "My Rank in Drawing Is A And This Equal 100 Points"
# # "My Rank in Sports Is C And This Equal 40 Points"
# # "Total Points Is 320"
#
# # Input
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
#
# my_points = {
#     'A': 100,
#     'B': 80,
#     'C': 40,
# }
#
# total = 0
# for rank in my_ranks:
#     print(f"My Rank in {rank} Is {my_ranks[rank]} And This Equal {my_points[my_ranks[rank]]}")
#     total += my_points[my_ranks[rank]]
# else:
#     print(f"Total Points Is {total}")
#
# # ------------------------------------------
# print("=" * 50)
# # ------------------------------------------
#
# # 04
# # Needed Output
# # "------------------------------"
# # "-- Student Name => Ahmed"
# # "------------------------------"
# # "- Math => 100 Points"
# # "- Science => 20 Points"
# # "- Draw => 80 Points"
# # "- Sports => 40 Points"
# # "- Thinking => 100 Points"
# # "Total Points For Ahmed Is 340"
# # "------------------------------"
# # "-- Student Name => Sayed"
# # "------------------------------"
# # "- Math => 80 Points"
# # "- Science => 80 Points"
# # "- Draw => 80 Points"
# # "- Sports => 20 Points"
# # "- Thinking => 100 Points"
# # "Total Points For Sayed Is 360"
# # "------------------------------"
# # "-- Student Name => Mahmoud"
# # "------------------------------"
# # "- Math => 20 Points"
# # "- Science => 100 Points"
# # "- Draw => 100 Points"
# # "- Sports => 80 Points"
# # "- Thinking => 80 Points"
# # "Total Points For Mahmoud Is 380"
#
# # Input
# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }
#
# # ال A تساوي 100 وال B تساوي 80 وال C تساوي 40 وال D تساوي 20
# chars = {
#     'A': 100,
#     'B': 80,
#     'C': 40,
#     'D': 20,
# }
#
# for main_key, main_value in students.items():
#     print("-" * 20)
#     print(f"Student Name: {main_key}")
#     print("-" * 20)
#     for child_key, child_value in main_value.items():
#         print(f"- {child_key} --> {chars[child_value]} Points")
#
# # ------------------------------------------
# # ------------------------------------------
# # ------------------------------------------
#
# print("#" * 50)
# print('تكليفات الدروس من الدرس 047 إلى 050')
# print("#" * 50)
#
# # 01
# # # Needed Output
# # Input
# # num = 0
# # "Number 0 Is Not Larger Than 0"
#
# # num = 10
# # # Needed Output
# # 9
# # 8
# # 7
# # 5
# # 4
# # 3
# # 2
# # 1
# # "8 Numbers Printed Successfully."
#
# num = int(input("Enter The Number : "))
# counter = 0
#
# if num <= 0:
#     print("Number 0 Is Not Larger Than 0")
# else:
#     while num > 0:
#         num -= 1
#         if num == 0:
#             break
#         if num == 6:
#             continue
#         counter += 1
#         print(num)
#     print(f"{counter} Numbers Printed Successfully.")

# ------------------------------------------
print("-" * 50)

# 02
# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"

# Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
#
# index = 0
# counter = 1
# print(len(friends))
#
# while index < len(friends):
#
#     if friends[index][0].isupper():
#         print(friends[index])
#     else:
#         counter += 1
#     index += 1
# print(f"Friends Printed And Ignored Names Count Is {counter}")
#
#
# # ------------------------------------------
print("-" * 50)

# # 03
# # قم بكتابة سطر واحد فقط لطباعة محتوى ال List كاملة
# # لا تقم بتعديل أي شيء في ال Code
# # Type The Code Here in One Line
# # Needed Output
# # "HTML"
# # "CSS"
# # "JavaScript"
# # "PHP"
# # "Python"
# # Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
#
# while skills:
#     print(skills.pop(0))

# # ------------------------------------------
print("-" * 50)

my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    remaining_slots = max_friends - len(my_friends)
    name = input("Enter the name of a friend to add ({} slots remaining): ".format(remaining_slots))
    name = name.strip()  # Remove leading and trailing spaces

    if name.isupper():
        print("Invalid name. Uppercase names are not allowed.")
    else:
        if name.islower():
            name = name.capitalize()
            print("First letter converted to uppercase.")

        my_friends.append(name)
        print("Added '{}' to the list.".format(name))

print("List is now full. Friends: ", my_friends)


# myFriends = []
# maxNum = 4
# name = input("Enter Your Name: ")
#
# while len(myFriends) < maxNum:
#     if name.isupper():
#         # print(name)
#         print("invalid name!")
#     else:
#         if name.islower():
#             name = name.capitalize();
#             myFriends.append(name)
#             print(f"Friend {name} Added => 1st Letter Become Capital")
#             maxNum -= 1
#             print(f"Names Left in List Is {maxNum}")
#         elif name[0].isupper():
#             myFriends.append(name)
#             print(f"Friend {name} Added")
#             maxNum -= 1
#             print(f"Names Left in List Is {maxNum}")
#         else:
#             print("---")
