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
if not (car < 10 and bike > 10):
    print('Either of the conditions are met')
    
