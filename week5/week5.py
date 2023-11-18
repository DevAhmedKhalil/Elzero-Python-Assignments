print("=" * 50)
print("تكليفات الدروس من الدرس 033 إلى 037")
print("=" * 50)

# 04
# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str'>
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000) / 5)
# print(type(((result ** 3) % 26000) / 5)) # <class 'float'>
print(type(str(((result ** 3) % 26000) / 5)))

print("=" * 50)

# 03
# Needed Output
# True
# False
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)

print("=" * 50)

# 02
# Needed Output
# True
html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript > 50)

print("=" * 50)

# 01
# Needed Output
# True
# True
# True
# True
# False
# False
# False
# False
print(bool(True))
print(bool("Ahmed"))
print(bool({1, 2, 3}))
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool(False))
print(bool(""))
print(bool({}))
print(bool([]))
print(bool(()))

print("=" * 50)
print("تكليفات الدروس من الدرس 038 إلى 040")
print("=" * 50)

# 01
# Input
# "     osAmA   "
# Needed Output
# "Hello Osama, Happy To See You Here."
# name = input("Enter Your Name: ")
# name = name.strip().capitalize()
# print(f"Hello {name}, Happy To See You Here :)")

# 02
# Inputs
# 16 # Input One
# 24 # Input Two
# Needed Output
# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

# age = int(input("Enter Your Age: ").strip())
# print(type(age))
#
# Age_Value_If_Larger_Than_16 = (age >= 16 and f"Hello Your Age Is {age}, All Articles Is Suitable For You")
# Age_Value_If_NOT_Larger_Than_16 = (age < 16 and "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
#
# print(Age_Value_If_Larger_Than_16)
# print(Age_Value_If_NOT_Larger_Than_16)


# 03
# Inputs
# "Osama" # First Name
# "Mohamed" # Second Name
# Needed Output
# "Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."
# fname = input("Enter Your First Name: ")
# mname = input("Enter Your Middle Name: ")
# lname = input("Enter Your Last Name: ")
#
# print(f"My Name: {fname.strip().capitalize()} {mname.strip().capitalize():.1s}. {lname.strip().capitalize()}")

# 04
# Inputs
# "Osama@Nn.Sa" # Email
# Needed Output
# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"
myEmail = input("Enter Your Email: ").strip()
print(f"Your Email IS: {myEmail}")

username = myEmail[:myEmail.index("@")]
print(f"username = {username}")

emailPrivider = myEmail[myEmail.index("@") + 1:myEmail.index(".")].lower()
print(f"Email Service Provider Is: {emailPrivider}")

domain = myEmail[myEmail.index(".") + 1:].lower()
print(f"Top Level Domain Is: {domain}")
