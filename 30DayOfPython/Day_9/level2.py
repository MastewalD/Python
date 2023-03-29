"""
score=input("Enter your score:")
if 80<int(score)<100:
    print("A")
elif 70<int(score)<89:
    print("B")
elif 60<int(score)<69:
    print("C")
elif 50<int(score)<59:
    print("D")
elif 0<int(score)<49:
    print("F")


month=input("Enter the month:")
if month =="September" or month =="October" or month =="November":
    print("Autumn")
elif month =="December" or month =="January" or month =="February":
    print("Winter")
elif month =="March" or month =="April" or month =="May":
    print("Spring")
elif month =="June" or month =="July" or month =="August":
    print("Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit =input("Enter the fruit:")
if fruit in fruits:
     print("That fruit already exist in the list")
else:
     fruits.append(fruit)
     print(fruits)
"""
