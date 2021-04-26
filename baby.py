#import the random and choice function
from random import choice

#List of choice questions
questions = ['while is sky blue: ', 'But What about the Moon: ', 'What about the sun?: ']

#Variable to call the choice function and pass it the list of choices
question = choice(questions)

#Baby first question
baby_question = input(question).strip().lower()

#As long as the Specified Answer for the baby is not in the Answer for the baby
while baby_question != 'just because':

    #Variable to call the choice function and pass it the list of choices
    question = choice(questions)

    #Baby continues question 
    baby_question = input(question).lower()
    
#Baby's Response as soon as the user gives an Answer that has the Specified Words in it
print("Okay, I am Happy now")