#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_negative = -last_digit

if last_digit == 0:
    print("Last digit of " + '{:d}'.format(number) + " is " +
          '{:d}'.format(last_digit) + " and is 0")
elif number < 0:
    print("Last digit of " + '{:d}'.format(number) + " is " +
          '{:d}'.format(last_digit_negative) +
          " and is less than 6 and not 0")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of " + '{:d}'.format(number) + " is " +
          '{:d}'.format(last_digit) + " and is less than 6 and not 0")
elif last_digit > 5:
    print("Last digit of " + '{:d}'.format(number) + " is " +
          '{:d}'.format(last_digit) + " and is greater than 5")
