#Q.no1
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

#Q.no2
print("Welcome to Treasure Land")
direction = input("Choose a direction, Either 'left' or 'right': ")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    action = input("Do you want to swim or wait?: ")
    if action == 'swim':
        print("Game Over")
    elif action == 'wait':
        color = input("Please Select a color: red, blue, or yellow: ")
        if color == 'red' or color == 'blue':
            print("Game Over")
        elif color == 'yellow':
            print("You Win!")
        else:
            print("Invalid Choice! Game Over")

 #Q.no4
x = int(input("Enter an integer: "))

if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("zero")

#Q.no5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#Q.no6
s1 = int(input("Enter marks for Subject 1: "))
s2 = int(input("Enter marks for Subject 2: "))
s3 = int(input("Enter marks for Subject 3: "))
s4 = int(input("Enter marks for Subject 4: "))

total = s1 + s2 + s3 + s4
percentage = total / 4

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Class"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)


#Q.no7 
cost_price = float(input("Enter the cost price of the bike: "))

if cost_price > 100000:
    tax = 0.15 * cost_price
elif cost_price > 50000:
    tax = 0.10 * cost_price
else:
    tax = 0.05 * cost_price

print("Road tax to be paid: Rs", tax)

#Q.no8

age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

youngest = min(age1, age2, age3, age4)

print("The youngest age is:", youngest)

#Q.no9
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

oldest = min(age1, age2, age3, age4)

print("The oldest age is:", oldest)

#Q.no10
marks = int(input("Enter your marks: "))

if marks < 25:
    grade = "D"
elif marks <= 45:
    grade = "C"
elif marks <= 50:
    grade = "B"
elif marks <= 60:
    grade = "B+"
elif marks <= 80:
    grade = "A"
else:
    grade = "A+"

print("Your grade is:", grade)

#Q.no11

salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the years of service: "))
if years_of_service > 10:
    bonus = 0.10 * salary
elif years_of_service >= 6:
    bonus = 0.08 * salary
else:
    bonus = 0.05 * salary
print("The bonus is: Rs", bonus)

#Q.no12
days = int(input("Enter the number of days: "))

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = 5 * 2 + (days - 5) * 3
elif days <= 15:
    charge = 5 * 2 + 5 * 3 + (days - 10) * 4
else:
    charge = 5 * 2 + 5 * 3 + 5 * 4 + (days - 15) * 5

print("Total charge is: Rs", charge)

#Q.no13
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = 0.05 * salary
else:
    bonus = 0

print("Net bonus amount: Rs", bonus)

#Q.no14
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius * radius
print("The area of the circle is:", area)

#Q.no15 
a = int(input("Enter the number of students in Class 1: "))
b = int(input("Enter the number of students in Class 2: "))
c = int(input("Enter the number of students in Class 3: "))
desks_a = (a + 1) // 2 
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

total_desks = desks_a + desks_b + desks_c

print("The smallest number of desks needed:", total_desks)

                                                        # To Be Continued: 



#Q.no16

N = int(input("Enter the number of students (N): "))
K = int(input("Enter the number of apples (K): "))
apples_per_student = K // N 
remaining_apples = K % N    

print(f"Each student gets {apples_per_student} apples.")
print(f"{remaining_apples} apples remain in the basket.")

#Q.no17
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Q.no18
city = input("Enter the name of the city: ").strip()
if city == "Delhi":
    print("The monument of Delhi is Red Fort.")
elif city == "Agra":
    print("The monument of Agra is Taj Mahal.")
elif city == "Jaipur":
    print("The monument of Jaipur is Jal Mahal.")
else:
    print("Sorry, I don't have information about that city.")

#Q.no19

number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by both 2 and 3.")
else:
    print(f"{number} is not divisible by both 2 and 3.")

#Q.no20

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0: 
        result = num1 / num2
    else:
        result = "undefined (division by zero is not allowed)"
else:
    result = "invalid operator"
print(f"Your Answer is: {result}")

 
#Q.no21
total_days = int(input("Enter the total number of days: "))
days_absent = int(input("Enter the total number of days absent: "))
days_attended = total_days - days_absent
percentage_attended = (days_attended / total_days) * 100
print(f"Percentage of classes attended: {percentage_attended:.2f}%")
if percentage_attended < 75:
    print("You are not eligible to sit in the exam.")
else:
    print("You are eligible to sit in the exam.")

#Q.no22
percentage = float(input("Enter your percentage: "))
if percentage < 40:
    category = "Failed"
elif 40 <= percentage < 55:
    category = "Fair"
elif 55 <= percentage < 65:
    category = "Good"
else:
    category = "Excellent"
print(f"Your category is: {category}")

#Q.no23
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").strip().upper()
days = int(input("Enter number of working days: "))

wage_per_day = 0
if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
elif 30 <= age <= 40:
    if gender == 'M':
        wage_per_day = 800
    elif gender == 'F':
        wage_per_day = 850
else:
    print("Age out of wage criteria.")
if wage_per_day > 0:
    total_wages = wage_per_day * days
    print(f"The total wages are: {total_wages}")

#Q.no24
a = True
b = True
c = True
d = True
print(c)                          
print(d)                          
print(not a)                      
print(not b)                      
print(not c)                    
print(not d)                    
print(a and b)                 
print(a or b)                     
print(a and b or c)               
print(not a or b or c)            
print(not a or not b or not c)    
print(not (not a or not b or not c))  

#Q.no25
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#Q.no26
correct_username = "admin"
correct_password = "password123"
username = input("Enter your username: ")

if username == correct_username:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Login successful! Welcome!")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found. Please check your username.")

#Q.no27
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")
    if num1 > 0:
        print("The number is positive.")
    elif num1 < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
    
#Q.no28
score = float(input("Enter your subject score: "))
if score > 90:
    print("Congratulations! You did an excellent job!")
elif 50 <= score <= 90:
    print("Good effort, but there's room for improvement. Keep working hard!")
else:
    print("Your score is below 50. It might be a good idea to retake the course and focus on mastering the subject.")

#Q.no29
age = int(input("Enter your age: "))

if age >= 18:
    degree = input("Do you have a degree? (yes/no): ").strip().lower()
    if degree == "yes":
        experience = float(input("Enter your years of work experience: "))
        if experience > 3:
            print("Highly Eligible.")
        elif 1 <= experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("You need a degree to be eligible for the job.")
else:
    print("You are not eligible as you are under 18.")

#Q.no30
weight = float(input("Enter the weight of the package (in kg): "))
if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 20
urgent = input("Is the delivery urgent? (yes/no): ").strip().lower()
if urgent == "yes":
    cost += 5 
print(f"The total delivery cost is: ${cost}")

#Q.no31
income = float(input("Enter your annual income: "))
if income >= 50000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 700:
        print("Loan approved with standard interest rate.")
    elif 600 <= credit_score <= 700:
        print("Loan approved with a higher interest rate.")
    else:
        print("Loan rejected due to low credit score.")
else:
    print("Loan rejected due to insufficient income.")


#Q.no32
weather = input("What is the weather like? (sunny/rainy): ")

if weather == "sunny":
    print("The weather is great! How about going for a hike or having a picnic?")
elif weather == "rainy":
    rain_gear = input("Do you have a raincoat or an umbrella? (yes/no): ")
    if rain_gear == "yes":
        print("You can visit a nearby mall or museum and enjoy your day!")
    else:
        print("It's best to stay home and watch some movies or relax indoors.")
else:
    print("Sorry, I can only suggest activities for sunny or rainy weather!")

#Q.no33
print("Welcome to the Haunted House")

choice1 = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()
if choice1 == "downstairs":
    print("Game Over")
else:
    choice2 = input("Do you want to 'enter the room' or 'stay outside'? ").lower()
    if choice2 == "enter the room":
        print("Game Over")
    else:
        choice3 = input("Choose between 'ghost', 'vampire', or 'werewolf': ").lower()
        if choice3 in ["ghost", "vampire"]:
            print("Game Over")
        elif choice3 == "werewolf":
            print("You Win")
        else:
            print("Invalid choice. Game Over")

#Q.no34
print("Welcome to the Jungle Adventure")

choice1 = input("Do you want to go 'left' or 'right'? ").lower()
if choice1 == "right":
    print("Game Over")
else:
    choice2 = input("Do you want to 'climb a tree' or 'explore the cave'? ").lower()
    if choice2 == "climb a tree":
        print("Game Over")
    else:
        choice3 = input("Choose between 'bear', 'tiger', or 'snake': ").lower()
        if choice3 in ["bear", "tiger"]:
            print("Game Over")
        elif choice3 == "snake":
            print("You Win")
        else:
            print("Invalid choice. Game Over")

#Q.no35
print("Welcome to the Magic Forest")

choice1 = input("Do you want to go 'north' or 'south'? ").lower()
if choice1 == "south":
    print("Game Over")
else:
    choice2 = input("Do you want to 'cross the river' or 'follow the path'? ").lower()
    if choice2 == "cross the river":
        print("Game Over")
    else:
        choice3 = input("Choose between 'fairy', 'ogre', or 'elf': ").lower()
        if choice3 in ["ogre", "fairy"]:
            print("Game Over")
        elif choice3 == "elf":
            print("You Win")
        else:
            print("Invalid choice. Game Over")

#Q.no36
print("Welcome to the Space Mission")

choice1 = input("Do you want to go 'to the moon' or 'to Mars'? ").lower()
if choice1 == "to mars":
    print("Game Over")
else:
    choice2 = input("Do you want to 'land on the surface' or 'stay in orbit'? ").lower()
    if choice2 == "land on the surface":
        print("Game Over")
    else:
        choice3 = input("Choose between 'alien', 'asteroid', or 'satellite': ").lower()
        if choice3 in ["alien", "asteroid"]:
            print("Game Over")
        elif choice3 == "satellite":
            print("You Win")
        else:
            print("Invalid choice. Game Over")

#Q.no37
print("Welcome to the Pirate Island")

choice1 = input("Do you want to go 'left' or 'right'? ").lower()
if choice1 == "right":
    print("Game Over")
else:
    choice2 = input("Do you want to 'dig for treasure' or 'sail the ship'? ").lower()
    if choice2 == "dig for treasure":
        print("Game Over")
    else:
        choice3 = input("Choose between 'shark', 'pirate ship', or 'mermaid': ").lower()
        if choice3 in ["shark", "pirate ship"]:
            print("Game Over")
        elif choice3 == "mermaid":
            print("You Win")
        else:
            print("Invalid choice. Game Over")

                                    #DONE











