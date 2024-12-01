
school = {
    "Class A": {
        "students": {
            "fazalullah": {"age": 10, "grade": "A"},
            "abdullah": {"age": 11, "grade": "B"}
        },
    },
    "Class B": {
        "students": {
            "sana": {"age": 12, "grade": "A"},
            "kifayat": {"age": 11, "grade": "C"}
        },
    }
}
print(school["Class A"]["students"])
print(school["Class A"]["students"]["fazalullah"]) 
print (school["Class A"]["students"]["fazalullah"]["age"])
print (school["Class B"]["students"]["kifayat"])