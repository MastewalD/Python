import math
lst=list()
print(lst)
lst =[]
print(lst)
lst=[1,2,3,4,5,6,]
print(lst)
print(len(lst))
first_item=lst[0]
last_item=lst[(len(lst) - 1)]
middle_item=lst[math.floor((len(lst)-1)/2)]
print(last_item)
print(first_item,middle_item,last_item)
mixed_data_types=["mastewal",23,1.73,"not married","addis ababa"]
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
first_company=it_companies[0]
middle_company=it_companies[math.floor((len(it_companies)-1)/2)]
last_company=it_companies[len(it_companies) -1]
print(first_company,middle_company,last_company)
it_companies[0]="Uber"
print(it_companies)
it_companies.append("Facebook")
print(it_companies)

it_companies.insert(math.floor((len(it_companies)-1)/2),"Maste")
print(it_companies)
print(first_company)
print(first_company.upper())

it_companies.extend("#")
print(it_companies)
does_exist="Kid" in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
three_company=it_companies[0:3]
print(three_company)
last_three_company=it_companies[-3:]
print(last_three_company)
midd=math.floor(((len(it_companies)-1)/2))

print(it_companies[midd:midd+1])
print(it_companies)


it_companies.pop(0)
print(it_companies)

del it_companies[midd]
print(it_companies)
del it_companies[(len(it_companies)-1)]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
print(it_companies)


