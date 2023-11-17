print("Assignment Week 3")

# --------------------------------------------------------------------------
# تكليفات الدروس من الدرس 019 إلى 020
print("تكليفات الدروس من الدرس 019 إلى 020".center(50, "*"))
# --------------------------------------------------------------------------

# 01
print("01 assignment1".center(30, "-"))
print(type(1))
print(type(1.123))
print(type(1.5j))

# 02
print("02 assignment1".center(30, "-"))
my_complex = 12 + 34j
print(my_complex.imag)
print(my_complex.real)

# 03
print("03 assignment1".center(30, "-"))
# Needed To be Output
# 10.0000000000
num = 10
print("{:.10f}".format(num))
print(format(num, ".10f"))

# 04
# Needed Output
# 159
# <class 'int'>
print("04 assignment1".center(30, "-"))
num = 159.650
print(int(num))
print(type(int(num)))

# 05
print("05 assignment1".center(30, "-"))
# 100 - 115 = -15
# 50 * 30 = 1500
# 21 % 4 = 1
# 110 / 11 = 10
# 97 // 20 = 4

# --------------------------------------------------------------------------
# تكليفات الدروس من الدرس 021 إلى 023
print("تكليفات الدروس من الدرس 021 إلى 023".center(50, "*"))
# --------------------------------------------------------------------------

# 01
# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
print("01 assignment2".center(30, "-"))
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))

# 02
# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
print("02 assignment2".center(30, "-"))
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

# 03
# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print("03 assignment2".center(30, "-"))
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:-1:1])
print(friends[-2::1])

# 04
# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
print("04 assignment2".center(30, "-"))
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-1] = "Elzero"
friends[-2] = "Elzero"
print(friends)

# 05
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
print("05 assignment2".center(30, "-"))
friends = ['Osama', "Ahmed", "Sayed"]
friends.insert(0, "Nasser")
friends.append("Salem")
print(friends)

# 06
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
print("06 assignment2".center(30, "-"))
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
print(friends.pop(0))
print(friends.pop(0))
print(friends)
print(friends.pop(-1))
print(friends)

# 07
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print("07 assignment2".center(30, "-"))
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
print(friends + employees + school)
# way 2
friends.extend(employees)
friends.extend(school)
print(friends)

# 08
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
print("08 assignment2".center(30, "-"))
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# 09
# Needed Output
# 6
print("09 assignment2".center(30, "-"))
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

# 10
# Needed Output
# Django
# Web
print("10 assignment2".center(30, "-"))
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][2])

# --------------------------------------------------------------------------
# تكليفات الدروس من الدرس 024 إلى 025
print("تكليفات الدروس من الدرس 024 إلى 025".center(50, "*"))
# --------------------------------------------------------------------------

# 01
# Needed Output
# "Osama"
# <class 'tuple'>
print("01 assignment3".center(30, "-"))
my_tuple = "Osama",
print(type(my_tuple))
my_tuple = ("Osama",)
print(type(my_tuple))

# 02
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
print("02 assignment3".center(30, "-"))
friends = ("Osama", "Ahmed", "Sayed")
a, b, c = friends
a = "Elzero"
friends = a, b, c
print(friends)
print(type(friends))
print(len(friends))

# 03
# Needed Output
# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
print("03 assignment3".center(30, "-"))
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(f"nums_and_letters_one = {nums_and_letters_one}")


# 04
# Needed Output
# 1
# 2
# 4
print("04 assignment3".center(30, "-"))
my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple
print(a)
print(b)
print(c)