print("تكليفات الدروس من الدرس 056 إلى 059")

print("-----------------------------------")
print("Assignment - (1)")
print("-----------------------------------")


def calculate(num1, num2, operation="add"):
    # Convert the operation to lowercase for validation
    operation = operation.lower()

    # Available operations
    available_operations = ["add", "subtract", "multiply", 'a', 's', "m"]

    # Check the validity of the operation
    if operation not in available_operations:
        return "Invalid operation"

    # Perform the calculation
    result = 0

    # print( f"+>> {operation[0]}")

    if operation == "add" or operation == operation[0]:
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2

    return result


# Example 1: Addition
print("Addition:", calculate(15, 5, "add"))

# Example 2: Subtraction
print("Subtraction:", calculate(15, 5, "subtract"))

# Example 3: Multiplication
print("Multiplication:", calculate(5, 5, "multiply"))

# Example 4: Default operation (Addition)
print("Default operation:", calculate(2, 2))

# Tests
print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30
#
print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10
#
print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200

print("-----------------------------------")
print("Assignment - (2)")
print("-----------------------------------")


def addition(*numbers):
    result = 0

    for num in numbers:
        if num == 10:
            continue
        elif num == 5:
            result -= num
        else:
            result += num

    return result


# Tests
print("Result 1:", addition(10, 20, 30, 10, 15))  # 65
# Output: Result 1: 6 (1 + 2 + 3 - 10 + 4 - 5 + 6)
print("Result 2:", addition(10, 20, 30, 10, 15, 5, 100))  # 160
# Output: Result 2: -15 (-5 - 5 - 5 - 5 - 5 - 5 - 5)

print("-----------------------------------")
print("Assignment - (3)")
print("-----------------------------------")


def show_skills(name, *skills):
    if skills:
        print(f"Hello {name} Your Skills IS: ")
        for skill in skills:
            print(skill)
    else:
        print(f"Hello {name} You Have No Skills To Show")


# Input
show_skills("Osama", "HTML", "CSS", "JS", "Python")

# # Output
# "Hello Osama Your Skills Is"
# "- HTML"
# "- CSS"
# "- JS"
# "- Python"

# Input
show_skills("Ahmed")

# Output
# "Hello Ahmed You Have No Skills To Show"

print("-----------------------------------")
print("Assignment - (4)")
print("-----------------------------------")


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} And Your Live In {country}"


# Input
print(say_hello("Osama", 38, "Egypt"))

# Output
# "Hello Osama Your Age Is 38 And You Live In Egypt"

# Input
print(say_hello())

# Output
# "Hello Unknown Your Age Is Unknown And You Live In Unknown"
