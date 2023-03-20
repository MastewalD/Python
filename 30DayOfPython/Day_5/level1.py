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