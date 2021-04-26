my_list = []

#Continue to Ask User for input while the length of the list is not reach the condition
while len(my_list) < 4:
    user_input = input("Enter a Name: ").title()
    my_list.append(user_input)
print("List is Now full")
print(my_list)