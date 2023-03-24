scor=input('Enter the score:')
if int(scor) >= 80 and int(scor) <=100:
    print('A')
elif int(scor) >=70 and int(scor) <=79:
    print('B')
elif int(scor) >=60 and int(scor) <=69:
    print('C')
elif int(scor) >=50 and int(scor) <=59:
    print('D')
else:
 print('F')


 month=input('Enter the month:')

if month == 'September' or month=='October' or month=='November' :
    print('Autumn')
elif month =='December' or month=='January ' or month=='February' :
    print('Winter')
elif month =='March' or month=='April ' or month=='May' :
    print('Spring ')
else:
    print('Summer')



    new_fruit=input('Enter the new fruit:')
fruits = ['banana', 'orange', 'mango', 'lemon']
if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)