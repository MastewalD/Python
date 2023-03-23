dog={}
print(type(dog))
dog["name"]="bob"
dog["color"]="black"
dog["breed"]="shapered"
dog["legs"]=4
dog["age"]=2
print(dog)
student={
    "first_name":"",
    "last_name":"" ,
    "gender":"",
    "age":"",
    "marital_status":"",
    "skills":[],
    "country":"",
    "city":"",
    "address":""

}
print(student)
print(len(student))
print(type(student.get("skills")))
student["skills"].append("React")
print(student["skills"])

print(student.keys())
print(student.values())
print(student.items())
del student["skills"]
print(student)
del student
print(student)
















