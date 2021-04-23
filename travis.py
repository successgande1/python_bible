known_users = ['Gande', 'Emma', 'Nabem', 'Jude', 'Blessing', 'Avalumun']

while True:
    user_name = input('What is your Name: ').capitalize()
    print(f'Hi! {user_name} welcome to Travis')

    #Check if user is in the list
    if user_name in known_users:
        print(f'Hello, {user_name}')
        
        #Ask User whether they would want to be removed from the list after making it lower case
        ask_remove = input('Would You like to be removed (y/n): ').lower()
        
        #Check if the user typed in Yes or No (y or n) which will to automatically lowered case
        if ask_remove == 'y':
            print(known_users)

            #Remove User from the List
            known_users.remove(user_name)
            print(f'{user_name}, You have been Removed from the System')
        #Else if user input is n (No) Display message for user
        elif ask_remove == 'n':
            print(f'Okay {user_name}, I did not want to remove you from the system either')

    else:
        print(f'Hmmm {user_name} we have not met before')

        #Ask User whether to be added to list
        ask_add = input('Would You like to be added to the System?: (y/n) ').lower()

        #Check if user input is 'y' (Yes) and then add him/her to the system
        if ask_add == 'y':
            
            #Add New User to the list
            known_users.append(user_name)
            print(f'{user_name}, You have now been added to the system successfully')
        elif ask_add == 'n':
            print(f'{user_name}, You have your right not to be added to our system')

