print("Assignment Week_1 Ass_2")

# 01 "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name, age, country = "Ahmed", "20", "Egypt"
print(f"\"Hello 'Osama', How You Doing \\ \"\"\" Your Age Is \"{age}\" + And Your Country Is: {country}")

# 02
# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt
print(f'''
"Hello '{name}', How You Doing \\
""" Your Age Is "{age}"" +
And Your Country Is: {country}
''')
print("\"Hello '%s', How You Doing \\ \n\
\"\"\" Your Age Is \"%s\" + \n\
And Your Country Is: %s \
" % (name, age, country))

# 03
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
name = 'Elzero'

print('Second Letter Is "{:s}"'.format(name[1]))
print('Third Letter Is "{:s}"'.format(name[2]))
print('Last Letter Is "{:s}"'.format(name[-1]))

# 04
# Needed Output
# "lze"
# "Ezr"
# "rzE"
name = 'Elzero'
#       012345
print(name[1:4])
print(name[::2])
print(name[0:5][-1::-2])

# 05
# Needed Output
# Elzero
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

# 06
# Needed Output
# # 0009
# # 0015
# # 0130
# # 0950
# # 1500
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# 07
# Needed Output
# # @@@@@@@@@@@@@@@Osama
# # @@@@@@@@Osama_Elzero
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# 08
name_one = "OSamA"
name_two = "osaMA"
# Needed Output
# osAMa
# OSAma
print(name_one.swapcase())
print(name_two.swapcase())

# 09
msg = "I Love Python And Although Love Elzero Web School"
# Needed To be Output
# 2
print(msg.count("Love"))

# 10
name = "Elzero"
# Needed To be Output
# 2
print(name.index("z"))

# 11
msg = "I <3 Python And Although <3 Elzero Web School"
# Needed To be Output
# I Love Python And Although <3 Elzero Web School
print(msg.replace("<3", "Love", 1))

# 12
msg = "I <3 Python And Although <3 Elzero Web School"
# Needed Output
# I Love Python And Although Love Elzero Web School
print(msg.replace("<3", "Love"))

# 13
name = "Osama"
age = 38
country = "Egypt"
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
print(f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}')
