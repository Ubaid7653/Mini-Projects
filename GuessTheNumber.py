#Guess the number game to generate a random number and input from user and check if the random number is equal to user input:

import random

#Guess the random Number from 1 to 20:
target=random.randint(1,20)

while True:
     user_input = input("Guess the Number or Quit(Q): ")  
     if (user_input=="q"):   #User Quit the game 
          break
      #User input is not Q then convert user value into integer
     user_input=int(user_input)
     #Check the condition:
     if (user_input==target): 
          print("Congratulations, you guessed the number correctly!")
          break
     elif (user_input<target): 
          print("Your Choice Value is too Small!.Guess the Big Value.....")
     else:
          print("your Choice Value is too Big!.Guess the Small Value.....")
print("_______________________Game Over________________________")

