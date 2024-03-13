#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ran_number = str(number)
ran_number = ran_number[-1:]
num_str = "Last digit of {} is {} "
if ran_number > '5' and number > 0:
    print(num_str.format(number, ran_number) + "and is greater than 5")
elif ran_number == '0':
    print(num_str.format(number, ran_number) + "and is 0")
elif ran_number < '6' and ran_number != '0' and number > 0:
    print(num_str.format(number, ran_number) + "and is less than 6 and not 0")
num_str = "Last digit of {} is -{} "
if ran_number != '0' and number < 0:
    print(num_str.format(number, ran_number) + "and is less than 6 and not 0")
