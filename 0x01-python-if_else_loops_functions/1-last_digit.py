#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ran_number = str(number)
ran_number = ran_number[-1:]
if ran_number > '5' and number > 0: 
    print("Last digit of {} is {} and is greater than 5".format(number, ran_number))
elif ran_number == '0':
    print("Last digit of {} is {} and is zero".format(number, ran_number))
elif ran_number < '6' and  ran_number != '0' and number > 0: 
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, ran_number))

elif ran_number != '0' and number < 0:
    print("Last digit of {} is -{} and is less than 6 and not 0".format(number, ran_number))
