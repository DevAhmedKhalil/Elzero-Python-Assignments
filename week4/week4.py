print("-" * 40)
print("تكليفات الدروس من الدرس 026 إلى 032")
print("-" * 40)

print("=" * 50)

# 01
# Needed Output
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list.pop())  # delete 5
print(unique_list)

print("=" * 50)

# 02
# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))

nums.update(letters)
print(nums)

for item in letters:
    nums.add(item)
print(nums)

print("=" * 50)

# 03
# Needed Output
# {1, 2, 3}
# set()
# {"A", "B"}
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)  # {1, 2, 3}
my_set.clear()
print(my_set)  # set()

letters.remove("C")
print(letters)  # {'B', 'A'}
print(my_set.union(letters))  # {'B', 'A'}

# 04
# Needed Output
# True
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

print("=" * 50)

# 05
# Needed Output :
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"
# Create Dictionary Here

my_skills = {
    "one": {
        "lang": "HTML",
        "progress": "70%"
    },
    "two": {
        "lang": "CSS",
        "progress": "80%"
    },
    "three": {
        "lang": "JS",
        "progress": "90%"
    },
}
print(my_skills)
print(f"HTML Progress Is {my_skills['one']['progress']}")
print("HTML Progress Is {:s}".format(my_skills['two']['progress']))
print("HTML Progress Is %s" % (my_skills['three']['progress']))

