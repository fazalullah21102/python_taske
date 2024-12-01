student = {
    "name": "Fazalullah",
    "roll_no": 161,
    "course": "BACS"
}

print(student)
print (student.get("roll_no"))  #accesoing elemant

student["name"] = "abdullah"    #appdating mathed 
print (student)

student["age"] = 18  #adding a new value
print (student)

del student["course"]  #delate a elemante
print(student)

print (student.keys())

print(student.values())

print("name" in student)

print(student.items())