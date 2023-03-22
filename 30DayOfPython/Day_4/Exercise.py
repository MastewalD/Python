import math
"""
print("Thirty "+"Days "+"Of "+"Python")

print("Coding "+"For "+"All")
"""
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.index("Coding"))
print(company.find("Coding"))
print(company.replace("Coding","Python"))
str="Python for Everyone "
str2=company.replace("Coding","Python")
print(str.replace(str,str2))

print(company.split())
str3="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str3.split(","))
str4=company.split()
print(str4[0])
print(str4[len(str4)-1])

print(company[10])
print(company.index("C"))
print(company.index("F"))
print(company.rindex("l"))
sentence= 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))
print(sentence.rindex("because"))
sentence1=sentence[31:54]
print((sentence1))
sentence2='You cannot end a sentence with because because because is a conjunction'
print(sentence2.index("because"))
print(company.startswith("Coding"))
print(company.endswith("coding"))
sentence5="30DaysOfPython"
sentence6="thirty_days_of_python"
print(sentence6.isidentifier())
print(sentence5.isidentifier())
frame_work=["Django","Flask","Bottle","Pyramid","Falcon"]
print(" ".join(frame_work))
sentence7="I am enjoying this challenge.\nI just wonder what is next."
print(sentence7)
sentence8="Name\tAge \tCountry \tcity\nAsabeneh\t250 \tFinland \tHelsinki"
print(sentence8)

















