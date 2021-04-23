known_users = ['Gande', 'Emma', 'Nabem', 'Jude', 'Blessing', 'Avalumun']

while True:
    user_name = input('What is your Name: ').capitalize()
    print(f'Hi! {user_name} welcome to Travis')

    #Check if user is in the list
    if user_name in known_users:
        print(f'Hello, {user_name}')
        
        #Ask User whether they would want to be removed from the list after making it lower case
        ask_user = input('Would You like to be removed (y/n): ').lower()
        
        #Check if the user typed in Yes or No (y or n) which will to automatically lowered case
        if ask_user == 'y':

            #Remove User from the List
            known_users.remove(user_name)

    else:
        print(f'{user_name} NOT Recognised')