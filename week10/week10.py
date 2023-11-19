print("-----------------------------------")
print("تكليفات الدروس من الدرس 069 إلى 071")
print("-----------------------------------")

print("-----------------")
print("Assignment 1")

values = (0, 1, 2)

if any(values):
    # true
    my_var = 0
#          0     1   2       3        4     5
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")
# Good => all(my_list[:4])  true

# --------------------------------------------------------------------------
print("-----------------")
print("Assignment 2")

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# print(pow(5, 5, 5))  # 0
# --------------------------------------------------------------------------

print("-----------------")
print("Assignment 3")

n = 20
l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")

# Output => Good

# This makes me Solve this Ass
# n = 20
# l = list(range(n))
#
# print(l)
# print("SUM ", round(sum(l)))
# print("ROUND ", round(sum(l) / n))

# --------------------------------------------------------------------------
print("-----------------")
print("Assignment 4")


def my_all(lst):
    for item in lst:
        if not item:
            return False
    return True


def my_any(lst):
    for element in lst:
        if element:
            return True
    return False


def my_min(nums):
    min_value = nums[0]
    for num in nums[1:]:
        if num < min_value:
            min_value = num

    return min_value


def my_max(nums):
    if not nums:
        raise ValueError("my_max() arg is an empty sequence")

    max_value = nums[0]
    for num in nums[1:]:
        if num > max_value:
            max_value = num

    return max_value


# my_all
print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False
print("-------------------")
# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False
print("-------------------")
# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100
print("-------------------")
# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700

# --------------------------------------------------------------------------
