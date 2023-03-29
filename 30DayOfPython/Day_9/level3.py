import math
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': [ 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
"""
if "skills" in person:
    skill=person["skills"]

    print(skill[math.floor((len(skill)-1)/2)])

if "skills"in person and "Python" in person["skills"]:
    print("skills"in person and "Python" in person["skills"])
    
if person["skills"] == ["Javascript","React"]:
    print("He is a front end developer ")
elif person["skills"] == ["Node","Python","MongoDB"]:
    print("He is a back end developer ")
elif person["skills"] == ["React","Node","MongoDB"]:
    print("He is a full stack developer ")
else:
    print("Unknown")


if person["is_marred"] == True and person["country"] =="Finland":
    print(person["first_name"],person["last_name"],"lives in ",person["country"],". He is married.")

"""


















