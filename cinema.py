#Dictionaries of films with list of age and number of tickets available for each film
films_age_tickets = {
    "Wars" : [18,3],
    "Tears" : [16,5],
    "Transporter" : [13,10],
    "Warriors" : [17,1],
    "Succeeder" : [19,7]
}

while True:
    #Request for User Film Choice and change it to title letters
    user_film_choice = input('Which Film would you want to book for?: ').title()
    
    #Check if user film choice is available
    if user_film_choice in films_age_tickets:

        #Request User Age and cast it into integer (Whole Number)
        user_age = int(input('How Old are You?: ').strip())

        #Check whether User Age is greater than or equal to the age for the choice film
        if user_age >= films_age_tickets[user_film_choice][0]:

            #Check for Number of Available Tickets using the dict index
            if films_age_tickets[user_film_choice][1] > 0:

                print(f'Have a nice time viewing {user_film_choice}')

                #Update the Number of Films left by minusing the dict index of age by 1
                films_age_tickets[user_film_choice][1] = films_age_tickets[user_film_choice][1]-1
            else:
                print(f'Sorry! {user_film_choice}, has no available Seats')
        else:
            print(f'You are too young to watch {user_film_choice}')
    else:
        print(f'ooops!, {user_film_choice} is NOT available')