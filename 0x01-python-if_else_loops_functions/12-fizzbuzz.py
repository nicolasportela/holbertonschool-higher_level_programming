#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 is 0 and n % 5 is not 0:
            print("Fizz", end=" ")
        elif n % 5 is 0 and n % 3 is not 0:
            print("Buzz", end=" ")
        elif n % 3 is 0 and n % 5 is 0:
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(n), end=" ")
