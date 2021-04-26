#Dictionary with List as value
students = {
    'Male' : ['Apollos', 'Gande', 'Jude', 'Avalumun', 'Kaka'],
    'Female' : ['Blessing', 'Msendoo', 'Happy', 'Alumun']
}

#For Loop and make the Dictionary Iterable by using the .key() method
for key in students.keys():
    for name in students[key]:
        if 'a' in name:
            print(name)
        