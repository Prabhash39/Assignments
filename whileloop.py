# 1. 

# while True:
#     age = input("Enter Your Age or stop to exit the code: ")
#     if age == "stop":
#      print("Exited")
#      break
#     age = int(age)
    
#     if age <= 18:
#         print("You are a minor")
    
#     elif age > 18 and age < 60:
#         print("You are an adult")

#     else:
#         print("You are a Senior Citizen")

    
# 2. 
# while True:
#     vehicle = input("What are you waiting for?: ").lower()
#     if vehicle == "bus":
#         print("Finally The wait is Over")
#         break

#     else:
#         print("Waiting")


# 3. 
# while True:
#     Fruit = input("Enter a fruit: ").lower()
#     if Fruit == "apple":
#         print("You Got It!")
#         break
#     else:
#         print("Try Again")


# 4.
# correct_password = "open sesame"
# while True:
#     Password = input("Enter the correct password: ")

#     if Password == "open sesame":
#         print("Acess Granted!")
#         break

#     else:
#         print("Wrong Password, try again")


# 5.

# while True:
#     week = input("Enter a day of the week: ")

#     if week != "sunday":
#         print("Its not the weekend yet")
#         break

#     else:
#         print("Enjoy Your WEEKEND!")



# 6. 

# import random

# secret_number = random.randint(1,10)

# attempts = 0

# while True:
#      guess = int(input("Guess a number between 1 and 10: "))
#      attempts += 1 

#      if guess <secret_number:
#           print("Guess Higher!")

#      elif guess > secret_number:
#           print("Guess Lower!")

#      else:
#           print(f"You guessed the correct answer in {attempts} attempts.")
#           break


# 7. 
# correct_username = "admin"
# correct_password = "1234"

# attempts = 3

# while attempts> 0:
#     username = input("Enter Your Username: ")
#     password = input("Enter Your Password")
    
#     attempts =- 1

    
#     if username == correct_username and password == correct_password:
#         print("Login successful")
       

#     else:
#         attempts -= 1

#         if attempts>0:
#              print(f"Invalid Credentials, Please Try again. You have {attempts} attempts left.")

#         else: 
#           print("Account Blocked")
#         break
    

#8
        
# import random  # Import random module

# while True:
#     num1 = random.randint(1, 30)  
#     num2 = random.randint(1, 30)  
#     correct_answer = num1 * num2  
    
#     while True:
#         user_input = input(f"What is {num1} * {num2}? (Type 'exit' to stop): ")

#         if user_input.lower() == "exit":
#             print("Quiz ended. Thanks for playing!")
#             exit()  

#         try:
#             user_answer = int(user_input)  # Convert input to an integer
#             if user_answer == correct_answer:
#                 print("Correct!")
#                 break  # Exit inner loop and generate a new question
#             else:
#                 print("Incorrect, try again.")
#         except ValueError:
#             print("Please enter a valid number or type 'exit' to stop.")

# #9
# import math

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# while True:
#     user_input = input("Enter a number to check if it's prime (or type 'exit' to stop): ")
    
#     if user_input.lower() == "exit":
#         break

#     try:
#         number = int(user_input)
#         if is_prime(number):
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")
#     except ValueError:
#         print("Please enter a valid number or type 'exit' to quit.")

#10
# secret_word = "python"

# while True:
#     guess = input("Guess the secret word (or type 'quit' to stop): ")

#     if guess.lower() == "quit":
#         print("Game exited.")
#         break

#     if guess.lower() == secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again.")

#11
# good_luck_count = 0

# while good_luck_count < 3:
#     phrase = input("Enter a phrase: ")

#     if phrase.lower() == "good luck":
#         good_luck_count += 1
#         if good_luck_count == 3:
#             print("You typed 'good luck' three times.")
#             break
#         else:
#             print(f"You typed the same word {good_luck_count} times.")