#Request for User Email and remain spaces
user_email = input('Enter Email Address:').strip()

#Slice Out Username 
user_name = user_email[:user_email.index('@'):1]

#Slice the email Domain Name. Add 1 to the @ symbol to get the a new slice start point without the @
domain_name = user_email[user_email.index('@') + 1 :]

#Format the message using the format string method
format_msg = "Your Username is {} and your Email Domain is {}".format(user_name.upper(), domain_name.capitalize())
#user_msg = 

#Display a Message
print(format_msg)