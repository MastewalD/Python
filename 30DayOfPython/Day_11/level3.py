import math


def add(num1,num2):
    sum=num1 + num2
    return sum
print(add(1,2))

def area_of_circle(radius):
    area=math.pi * radius **2
    return area
print(area_of_circle(10))

def add_all_number(*nums):
    sum=0
    for num in nums:
        sum = sum +num
    return sum
print(add_all_number(10,10,10))
