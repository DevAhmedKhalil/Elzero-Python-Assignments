print('#' * 50)
print("تكليفات الدروس من الدرس 090 إلى 094")
print("#" * 50)

print("التكليف 01")
print("----------")

NUM = input("Add Your Number: ")
try:
    if not NUM.isdigit():
        raise Exception()

    num = int(NUM)

    if num > 10:
        raise IndexError("IndexError: Only One Character Allowed")

    elif num <= 0:
        raise ValueError("ValueError: Number Must Be Larger Than 0")

    print("#" * 20)
    print(f"The Number Is {num}")
    print("#" * 20)

except ValueError as ve:
    print(ve)

except IndexError as ie:
    print(ie)

except Exception:
    print("Exception: Only Numbers allowed")

print("----------")
print("التكليف 02")
print("----------")

LETTER = input("Add Letter From A to Z: ")

try:
    if len(LETTER) != 1:
        raise ValueError("You Must Write One Character Only")

    if not ('A' <= LETTER <= 'Z'):
        raise ValueError("The Letter Not In A - Z")

except ValueError as ve:
    print(ve)

else:
    print(f"You Typed {LETTER}")

print("----------")
print("التكليف 03")
print("----------")


def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30)) # 50
