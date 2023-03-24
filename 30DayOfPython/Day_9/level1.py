import math
"""
age=input("Enter your age:")
remain=18 -int(age)
if int(age) >= 18:
    print("You are old enough to drive.")
else:
    print("You need " ,remain ,"more years to learn to drive")
"""
yourAge=input("Enter your age:")
difference=25-int(yourAge)
if difference > 0:
    print("You are ",difference,"year younger than me")
else:
    print("You are ",math.abs(difference),"year older than me ")