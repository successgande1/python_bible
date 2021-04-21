#Using Lists, Dictionaries, and Topples to create different Data Types in one variable
my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)

#List can contain inside it different data types like string, numbers, booleans etc
apollos = ['Gande', 'Blessing', 1,3,5, True, False]
print(apollos)

#List are immutable and iterable so can be accessed using index
print(apollos[4])
other_list = apollos[apollos.index(1):apollos.index(False)]
print(other_list)