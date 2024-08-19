import random
import string

#Guess the character in the list using random choice :
pass_len=12
pass_char= string.ascii_letters + string.digits +string.punctuation

#Start the loop for taking character and put into your password variable
password=""
for i in range(pass_len):
     password+=random.choice(pass_char)

#print the password:
print("Your Password is :",password)