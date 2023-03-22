import math
age=23
height=1.73
complex=2 +2j

print(type(complex))
base=input("Enter base ")
height=input("Enter height ")
area_of_rectangle=int(base) *int(height)
print("The area of the triangle is ",area_of_rectangle)



a=input("Enter side a:")
b=input("Enter side b:")
c=input("Enter side c:")
perimeter =int(a) +int(b)+int(c)
print("The perimeter of the triangle is ", perimeter)


length= input("Enter the length:")
width=input("Ente the width:")
area=int(length) *int(width)
print("The area of rectangle is :",area)




radius=input("Enter the radius of the circle:")
area = math.pi*(int(radius)**2)
perimeter=2*math.pi*int(radius)
print("The area and circumfrance of the circle is ",area,perimeter)

y1=0
x1=(y1+2)/2
x_intercept=(x1,y1)


x2=0
y2=2*x2-2
y_intercept=(x2,y2)

slop=(y2-y1)/(x2 - x1)
print(slop)



x1=2
y1=2
point1=(x1,y1)
x2=6
y2=10
point2=(x2,y2)

m=(y2-y1)/(x2-x1)
d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(m)
print(d)

print(slop == m)

len_python=len("python")
len_jargon=len("jargon")
print(len_python !=len_jargon)
print("on" in ("python" and "jargon"))
sentence="I hope this course is not full of jargon"
print("jargon" in sentence)
print("on" not in ("python" and "jargon") )

str="python"
float_number=float(len(str))
print(str(float_number))

var1=math.floor(7/3)
print(var1 == int(2.7))

print("10" ==10)
print(int(9.8)==10)

hours=input("Enter hours:")
rate_per_hour=input("Enter rate per hour:")
pay=int(hours)*int(rate_per_hour)
print("Your weekly earning is " , pay)


year=input("Enter number of years you have lived:")
second=int(year)*365*24*60*60
print("You have lived for " ,second,"seconds.")


print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')













