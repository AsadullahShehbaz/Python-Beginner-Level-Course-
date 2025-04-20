student = {
     "name": "Abdul Qadir",
     "class": 12,
     "section":"Prince"
}

# print(student.clear())

# sect = student.pop("section","default")
# print(sect)
# student.popitem()

# print(student.values())
new_student = student.fromkeys(student, 0 )
print(new_student.values())