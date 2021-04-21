#Using the OR and AND Logic operations
C = 7
D = 6

#This Condition will evaluate to True becos on of them is True (Start From Left Bracket)
if (C > 7 and D > 5) or (C < 10 and D == 6):
    print('It worked')
else:
    print('It Did Not Worked')

#This Condition will evaluate to False becos the NOT operator reverses the result orderwise
#The NOT Logic Operator change the result from True to False and verse Versa
if not ((C > 7 and D > 5) or (C < 10 and D == 6)):
    print('It worked')
else:
    print('It Did Not Worked')