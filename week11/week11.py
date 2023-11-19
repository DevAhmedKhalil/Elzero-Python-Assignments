print("#" * 50)
print("تكليفات الدروس من الدرس 076 إلى 078")
print("#" * 50)

# print("التكليف 01")
# print("#" * 50)

import random

# from random import randrange, randint

random_number_range_10_50 = random.randrange(10, 51)
print(f"Random Number Between 10 And 50 => {random_number_range_10_50}")

random_even_number_between_2_10 = random.randint(2, 5) * 2
print(f"Random Even Number Between 2 And 10 => {random_even_number_between_2_10}")

random_odd_number_between_1_9 = random.randint(1, 4) * 2 - 1
print(f"Random Odd Number Between 1 And 9 => {random_odd_number_between_1_9}")

# print(dir(random))

# print("#" * 50)

print("#" * 50)
print("تكليفات الدروس من الدرس 079 إلى 080")
print("#" * 50)

print("-" * 20)
print("التكليف 01")
print("-" * 20)

import datetime

date1 = datetime.datetime(2021, 6, 25)
date2 = datetime.datetime(2021, 8, 10)

print(f"Days From 2021-06-25 To 2021-08-10 Is => {(date2 - date1).days}")

# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"

print("-" * 20)
print("التكليف 02")
print("-" * 20)

# Today Is "2021, 8, 10"
day = datetime.datetime(2021, 8, 10)

print(day.strftime("%Y-%m-%d"))  # "2021-08-10"
print(day.strftime("%b %d, %Y"))  # "Aug 10, 2021"
print(day.strftime("%d - %b - %Y"))  # "10 - Aug - 2021"
print(day.strftime("%d / %b / %y"))  # "10 / Aug / 21"
print(day.strftime("%d / %B / %Y"))  # "10 / August / 2021"
print(day.strftime("%a, %d %B %Y"))  # "Tue, 10 August 2021"

print("#" * 50)
print("تكليفات الدروس من الدرس 081 إلى 085")
print("#" * 50)

print("-" * 20)
print("التكليف 01")
print("-" * 20)


def reverse_string(my_string):
    yield my_string[-1]
    yield my_string[-2]
    yield my_string[-3]
    yield my_string[-4]
    yield my_string[-5]
    yield my_string[-6]


# Reverse The String
for c in reverse_string("Elzero"):
    print(c, end="")

# -------------------------------------------------------------
print("\n")


def reverse_string(my_string):
    # يقوم بعكس النص ويستخدم yield لإرجاع الأحرف بشكل تتابعي
    for char in reversed(my_string):
        yield char


# Reverse The String
for c in reverse_string("Elzero"):
    print(c, end="")

# -------------------------------------------------------------
print("\n")
print("-" * 20)
print("التكليف 02")
print("-" * 20)


# Create Your Decorator Here
def myDecorator(func):
    def myFunc():
        print("Sugar Added From Decorators")
        func()
        print("####################")

    return myFunc


@myDecorator
def make_tea():
    print("Tea Created")


@myDecorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()

# Needed Output
# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"
