#Ask User for Name
user_name = input("What is your Name: ")


#Ask User for Age
user_age = int(input("How Old Are You?: "))


#Ask User for City
user_city = input("Which City Do you Live In: ")

#Ask User for What they Enjoy
user_love = input("What Do You Love Most: ")

#Message Template
string_msg = "Hellow {}, you are {} years old, you live in {} Town and you love {}"
format_msg = string_msg.format(user_name, user_age, user_city, user_love)
#Display Message
print(format_msg)
