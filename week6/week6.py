print("=" * 50)
print("تكليفات الدروس من الدرس 041 إلى 046")
print("=" * 50)

# 01
# Needed Output
# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800
# Inputs

# num1 = int(input("Enter Num 1: ").strip())
# operation = input("Enter any operation +, *, -, /: ").strip()
# num2 = int(input("Enter Num 2: ").strip())
#
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     print("Error... Only have this operation +, *, -, /")
#
# print(f"Example One {num1} {operation} {num2} = {result}")
# print("-" * 50)


# 02
# Needed Output
# "App Is Suitable For You" # If Age Larger Than 6
# "App Is Not Suitable For You" # if Age Smaller Than 16

# age = 17
# check = "App Is Suitable For You" if age > 16 else "App Is Not Suitable For You"
# print(check)
# print("-" * 50)

# 03
# Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example
# Input Example 38

# age = int(input("Enter Your Age Here: ").strip())
# if 10 < age < 100:
#     print("Your Age in monthes is: {:,d} month".format(age * 12))
#     print("Your Age in weeks is: {:,d} week".format(age * 12 * 4))
#     print("Your Age in days is: {:,d} day".format(age * 12 * 4 * 7))
#     print("Your Age in hours is: {:,d} hour".format(age * 12 * 4 * 7 * 24))
#     print("Your Age in minutes is: {:,d} min".format(age * 12 * 4 * 7 * 24 * 60))
#     print("Your Age in seconds is: {:,d} sec".format(age * 12 * 4 * 7 * 24 * 60 * 60))
# else:
#     print("age must be > 10 and < 100")


# 04
# Needed Output
# # "Your Country Eligible For Discount And The Price After Discount Is $70"  # Egypt Example
# # "Your Country Not Eligible For Discount And The Price Is $100"  # Ghana Example
# #
# Input Example One "Egypt"
# Input Example Two "Ghana"
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print("Your Country Eligible For Discount And The Price After Discount Is ${:d}".format(price - discount))
else:
    print("Your Country Not Eligible For Discount And The Price Is $%.2f" % price)
