from functools import reduce

print("-----------------------------------")
print("تكليفات الدروس من الدرس 072 إلى 075")
print("-----------------------------------")

print("Assignment 1")
print("++++++++++++++++++++++++")

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]


def remove_chars(text):
    return f"{text[1:-1]}"


# print(remove_chars(friends_map[0]))

cleaned_list = map(remove_chars, friends_map)
# print(cleaned_list) #<map object at 0x00000176dcff6050>

for name in cleaned_list:
    print(name)

print("#" * 10)

for n in map(lambda el: el[1:-1], friends_map):
    print(n)

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

print("++++++++++++++++++++++++")
print("Assignment 2")
print("++++++++++++++++++++++++")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def get_names(name1):
    if name1.endswith('m'):
        return name1
    return False


names = filter(get_names, friends_filter)

for name in names:
    print(name)

# print(get_names(friends_filter[0])) #False

# Output
# "Wessam"
# "Essam"

print("++++++++++++++++++++++++")
print("Assignment 3")
print("++++++++++++++++++++++++")

nums = [2, 4, 6, 2]


def mulAll(num1, num2):
    return num1 * num2


result = reduce(mulAll, nums)

print(result)

result2 = reduce(lambda num1, num2,: num1 * num2, nums)

print(result2)

# Output
# 96

print("++++++++++++++++++++++++")
print("Assignment 4")
print("++++++++++++++++++++++++")

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for i, item in enumerate(reversed(skills), 50):
    if isinstance(item, str):
        print(f"{i} - {item}")

print("#" * 10)

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

index = 49  # بدء العداد من 50

for item in reversed(skills):
    index += 1
    if isinstance(item, str):
        print(f"{index} - {item}")

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"
