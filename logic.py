#The NOT logical operator
car = 10
bike =15

if not car < bike:
    print('Number of cars are higher than bikes')
else:
    print('The Number of Bikes are Higher than Cars')



#The AND Operator
'''THE AND GATE
True and True = True
False and True = False
True and False = False '''

if car < 10 and bike > 10:
    print('Cars are less than 10 and Bikes are higher than 10')
elif car <= 10 and bike > 10:
    print('Cars are less than or equal to 10 and Bikes are higher than 10')
else:
    print('Either of the conditions are met')

#The NOT and the AND with brackets (Remember BODMAS and evaluate the conditions in the bracket first)
''' The conditions inside the brackets are evaluated first
 and if the result is True then the NOT outside the brackets 
 makes it False and verse versa '''
if not (car <= 10 and bike > 10):
    print('Car less than 10 and bike greater than 10')
else:
    print('The NOT evaluates the Result otherwise')

#The OR Operator
''' The OR Logic Gate demands that
 if Two Conditions are True then it results to True,
 if one condition is True and another False it evaluated 
 to True, if 1st condition is False and another True it 
  evaluates to True, if Two conditions are False then 
 it evaluates to False'''
phone = 6
chair = 4
#This will print the if conditional message becos one of the conditions is True
if phone > 6 or chair > 2:
    print('It worked')
else:
    print('It did not work')

