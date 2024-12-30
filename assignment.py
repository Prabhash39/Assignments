
#Q.NO1
a = '1'
b = '2'
if a == b:
  print('1')
if a>b :
  print ('2')
else:
  print ('3')

#Q.NO2
a = int(input("Enter a number:"))
if a %2 == 0:
    print("The number is even.")
else:
    print("The number is odd")
'''
'''
#Q.no 3
a = int(input("Enter a month 1-12: "))
if a>12 or a<1:
    print("Error. Please write a number from 1-12: ")
else:
    if a==1:
     print("janurary")
    if a==2:
        print("feburary")
    if a==3:
            print("march")
    if a==4:
                print("april")
    if a==5:
                    print("may")
    if a==6:
                        print("june")
    if a==7:
                            print("july")
    if a==8:
                                print("august")
    if a==9:
                                    print("september")
    if a==10:
                                        print("october")
    if a==11:
                                            print("november")
    if a==12:
                                                print("December")

#Q.no4
Marks = int(input("Enter your marks to get your corresponding grade: "))
if Marks < 0 or Marks > 100:
    print("Invalid Marks. Marks can only be from 0-100:")
else:

  if Marks < 25:
    print("Your Grade is F")
  elif 25 <= Marks <= 45:
    print("Your Grade is E")
  elif 45 <= Marks <=50:
    print("Your Grade is D")
  elif 50 <= Marks <= 60:
    print("Your Grade is C")
  elif 60 <= Marks <= 80:
    print("Your Grade is B")
  elif Marks>80:
    print("Your Grade is A")

#Q.no5
#     

a = int(input("Enter a number to check if it is divisible by 7 or not:"))

if a % 7 ==0:
  print(f"{a}is divisible by 7")
else:
  print(f"{a} is not divisible by 7")

#Q.no6
a = int(input("Enter first number"))

b = int(input("Enter second number"))

print(f"Your Answer is {a+b}")

#Q.no7
a = int(input("Enter 5 for 'HI' otherwise bye:"))

if a == 5:
 print("HI")
elif a>5 or 5>a:
 print("BYE")

 #Q.no8
 
n = int(input("Enter an integer n to check if it is divisible by 3 and 5:"))

if n % 3 == 0 & n % 5 == 0:
 print("FizzBuzz")

elif n % 3 == 0:
 print("Fizz")
 
elif n % 5 == 0:
 print("Buzz")
else:
 print("n")

 # Q.no 9


char = input("Enter a single character: ").lower()
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")
else:
    print("Please enter a valid single alphabet character.")

#Q.10

marks = int(input("Enter your marks (0-100): "))
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
elif 0 <= marks < 70:
    grade = "Fail"
else:
    grade = "Invalid marks. Please enter a number between 0 and 100."
print(f"Your grade: {grade}")

#Q.11

age = int(input("Enter the person's age: "))
if age < 13:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif age > 19:
    category = "Adult"
else:
    category = "Invalid age"
print(f"The person is categorized as: {category}")

#Q.12
char = input("Enter a single character: ")

if len(char) == 1:
    if char.isupper():
        print(f"'{char}' is an uppercase letter.")
    elif char.islower():
        print(f"'{char}' is a lowercase letter.")
    elif char.isdigit():
        print(f"'{char}' is a digit.")
    else:
        print(f"'{char}' is neither an uppercase letter, a lowercase letter, nor a digit.")
else:
    print("Please enter only a single character.")

  #Q.no13

color = input("Enter a color (Red, Yellow, Green): ").strip().lower()
if color == "red":
    action = "Stop"
elif color == "yellow":
    action = "Get Ready"
elif color == "green":
    action = "Go"
else:
    action = "Invalid color. Please enter Red, Yellow, or Green."
print(action)

#Q.no14

age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))
if age > 18 and experience >= 2:
    print("You are Eligible for the job.")
else:
    print("You are Not Eligible for the job.")

#Q.no15
temperature = float(input("Enter the temperature in °C: "))

if temperature > 30:
    advice = "It's hot, stay hydrated!"
elif 15 <= temperature <= 30:
    advice = "Enjoy the weather!"
else:  # temperature < 15
    advice = "It's cold, wear warm clothes!"
print(advice)

#Q.no16
menu_item = input("Enter a menu option (Pizza, Burger, Pasta): ").strip().lower()
if menu_item == "pizza":
    price = "$10"
elif menu_item == "burger":
    price = "$7"
elif menu_item == "pasta":
    price = "$8"
else:
    price = "Invalid option. Please choose Pizza, Burger, or Pasta."
print(price)

#Q.no17
height = float(input("Enter the player's height in feet: "))
if height >= 6:
    result = "Selected"
else:
    result = "Not Selected"
print(result)

#Q.no18
age = int(input("Enter your age: "))
if age >= 18:
    result = "Allowed"
else:
    result = "Not Allowed"
print(result)

#Q.no19
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")

#Q.no20
month = int(input("Enter the month number (1-12): "))
if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
elif month in [9, 10, 11]:
    season = "Autumn"
else:
    season = "Invalid month number. Please enter a number between 1 and 12."
print(season)

#Q.no21
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 50000 and credit_score >= 700:
    result = "Eligible"
else:
    result = "Not Eligible"
print(result)

#Q.no22
number = int(input("Enter a number: "))
if 1 <= number <= 100:
    print(f"The number {number} is between 1 and 100.")
else:
    print(f"The number {number} is NOT between 1 and 100.")
                    #DONE