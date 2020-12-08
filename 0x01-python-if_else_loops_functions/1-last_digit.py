#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, "is", end=" ")
absolute = abs(number)
last_digit = absolute % 10
if number < 0:
    print(-last_digit, end=" ")
else:
    print(last_digit, end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and not 0:
    print("and is less than 6 and not 0")
