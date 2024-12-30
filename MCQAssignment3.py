#1.
price = float(input("Enter the price of the item: "))
if price > 1000:
    final_price = price * 0.9
elif price > 500:
    final_price = price * 0.95
else:
    final_price = price
print(f"Final price: {final_price}")

#2.
choice = input("Do you want vegetarian or non-vegetarian? ").lower()
if choice == "vegetarian":
    dish = input("Do you want 'Salad' or 'Pasta'? ").lower()
    print(f"You chose {dish}.")
elif choice == "non-vegetarian":
    dish = input("Do you want 'Chicken' or 'Fish'? ").lower()
    print(f"You chose {dish}.")
else:
    print("Invalid choice.")

#3.
salary = float(input("Enter the employee's monthly salary: "))
if salary > 50000:
    print("High Earner")
elif salary > 20000:
    print("Mid Earner")
else:
    print("Low Earner")

#4.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Divisible by 2")
    if number % 5 == 0:
        print("Also divisible by 5")
else:
    print("Not divisible by 2")

#5.
marks = float(input("Enter the student's marks: "))
if marks > 50:
    if marks > 90:
        print("Excellent")
    else:
        print("Good")
else:
    print("Fail")

#6.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print(f"The largest number is {largest}")

#7.
print("Welcome to the Forest Adventure")
path = input("Do you want to go 'left' or 'right'? ").lower()
if path == "left":
    action = input("Do you want to 'explore' or 'rest'? ").lower()
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice.")
elif path == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid choice.")

#8.
print("Welcome to the Jungle Survival Challenge")
action = input("Do you want to 'search for food' or 'build a shelter'? ").lower()
if action == "search for food":
    sub_action = input("Do you want to 'hunt' or 'gather'? ").lower()
    if sub_action == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif sub_action == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice.")
elif action == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid choice.")

#9.
print("Welcome to the Space Adventure")
choice = input("Do you want to 'land on Mars' or 'fly to Jupiter'? ").lower()
if choice == "land on mars":
    sub_choice = input("Do you want to 'explore' or 'build a base'? ").lower()
    if sub_choice == "explore":
        print("You found alien artifacts. You Win!")
    elif sub_choice == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice.")

#10.
print("Welcome to the Haunted Castle")
choice = input("Do you want to 'enter the castle' or 'run away'? ").lower()
if choice == "enter the castle":
    door = input("Choose a door: 'red', 'green', or 'black': ").lower()
    if door == "red":
        print("You entered a room full of flames. Game Over.")
    elif door == "green":
        print("You found the treasure. You Win!")
    elif door == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice.")

#11.
print("Welcome to the Underwater World")
choice = input("Do you want to 'dive deeper' or 'surface'? ").lower()
if choice == "dive deeper":
    sub_choice = input("Do you want to 'search for pearls' or 'chase the fish'? ").lower()
    if sub_choice == "search for pearls":
        print("You found a rare pearl. You Win!")
    elif sub_choice == "chase the fish":
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "surface":
    print("You returned safely.")
else:
    print("Invalid choice.")

#12.
print("Welcome to the Pirate Ship Adventure")
choice = input("Do you want to 'search for treasure' or 'battle enemy ships'? ").lower()
if choice == "search for treasure":
    sub_choice = input("Do you want to 'dig on the island' or 'explore the cave'? ").lower()
    if sub_choice == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif sub_choice == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "battle enemy ships":
    sub_choice = input("Do you want to 'attack' or 'defend'? ").lower()
    if sub_choice == "attack":
        print("You won the battle. You Win!")
    elif sub_choice == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")

#13.
print("Welcome to the Wizarding World")
choice = input("Do you want to study 'spells' or 'potions'? ").lower()
if choice == "spells":
    sub_choice = input("Do you want to 'practice magic' or 'compete in duels'? ").lower()
    if sub_choice == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif sub_choice == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "potions":
    sub_choice = input("Do you want to 'brew an elixir' or 'create poison'? ").lower()
    if sub_choice == "brew an elixir":
        print("You healed a village. You Win!")
    elif sub_choice == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")

#14.
print("Welcome to the Cybersecurity Mission")
choice = input("Do you want to 'trace the hacker' or 'secure the system'? ").lower()
if choice == "trace the hacker":
    sub_choice = input("Do you want to 'track their IP' or 'decode their message'? ").lower()
    if sub_choice == "track their IP":
        print("You caught the hacker. You Win!")
    elif sub_choice == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "secure the system":
    sub_choice = input("Do you want to 'shut down the server' or 'upgrade the firewall'? ").lower()
    if sub_choice == "shut down the server":
        print("The attack was stopped. You Win!")
    elif sub_choice == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")

#15.
number = int(input("Enter a number: "))
if number % 2 == 0 and number % 7 == 0:
    print("Double Seven")
elif number % 2 == 0:
    print("Even")
elif number % 7 == 0:
    print("Lucky Seven")
else:
    print(number)

#16.
number = int(input("Enter a number: "))
if number > 100:
    print("Big Number")
elif 50 <= number <= 100:
    print("Medium Number")
else:
    print("Small Number")

#17.
color = input("Enter a color: ").capitalize()
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Slow Down")
elif color == "Green":
    print("Go")
else:
    print("Invalid Signal")

#18.
temp = float(input("Enter the temperature in Celsius: "))
if temp > 40:
    print("Hot")
elif 20 <= temp <= 40:
    print("Warm")
else:
    print("Cold")

#19.
bmi = float(input("Enter your BMI value: "))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

#20.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print(f"Sum: {num1 + num2}")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print(f"Difference: {abs(num1 - num2)}")
else:
    print(f"Product: {num1 * num2}")

#21.
price = float(input("Enter the price of the item: "))
if price > 1000:
    print(f"New price after 20% discount: {price * 0.8}")
elif 500 <= price <= 1000:
    print(f"New price after 10% discount: {price * 0.9}")
else:
    print(f"No discount applied. Price: {price}")

#22.
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
income = float(input("Enter your annual income: "))
if age >= 18 and age < 60:
    if gender == "M":
        if income > 1000000:
            tax = income * 0.3
        elif income > 500000:
            tax = income * 0.2
        else:
            tax = income * 0.1
    elif gender == "F":
        if income > 1000000:
            tax = income * 0.25
        elif income > 500000:
            tax = income * 0.15
        else:
            tax = income * 0.05
elif age >= 60:
    if income > 1000000:
        tax = income * 0.2
    else:
        tax = income * 0.1
else:
    tax = 0
print(f"Your tax is: {tax}")

#23.
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
score = int(input("Enter your academic score: "))
if 18 <= age <= 25:
    if gender == "M":
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == "F":
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
else:
    print("Not eligible")

#24.
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
experience = int(input("Enter your years of experience: "))
if 21 <= age <= 35:
    if gender == "M":
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == "F":
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
elif age > 35:
    print("Manager Role")
else:
    print("Not eligible")

#25.
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
show_type = input("Enter the show type (Matinee/Evening): ").capitalize()
if age < 12:
    if show_type == "Matinee":
        print("Ticket = Rs500")
    elif show_type == "Evening":
        print("Ticket = Rs700")
    else:
        print("Invalid show type")
elif 12 <= age < 60:
    if gender == "M":
        if show_type == "Matinee":
            print("Ticket = Rs800")
        elif show_type == "Evening":
            print("Ticket = Rs1000")
        else:
            print("Invalid show type")
    elif gender == "F":
        if show_type == "Matinee":
            print("Ticket = Rs700")
        elif show_type == "Evening":
            print("Ticket = Rs900")
        else:
            print("Invalid show type")
    else:
        print("Invalid gender")
elif age >= 60:
    if show_type in ["Matinee", "Evening"]:
        print("Ticket = Rs600")
    else:
        print("Invalid show type")
else:
    print("Invalid age")

#26.
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
membership = input("Enter membership type (Monthly/Yearly): ").capitalize()
if 18 <= age < 30:
    if gender == "M":
        if membership == "Monthly":
            print("Rs50")
        elif membership == "Yearly":
            print("Rs500")
        else:
            print("Invalid membership type")
    elif gender == "F":
        if membership == "Monthly":
            print("Rs45")
        elif membership == "Yearly":
            print("Rs450")
        else:
            print("Invalid membership type")
    else:
        print("Invalid gender")
elif 30 <= age <= 50:
    if membership == "Monthly":
        print("Rs60")
    elif membership == "Yearly":
        print("Rs600")
    else:
        print("Invalid membership type")
elif age > 50:
    if membership == "Monthly":
        print("Rs40")
    elif membership == "Yearly":
        print("Rs400")
    else:
        print("Invalid membership type")
else:
    print("Invalid age")

                            #DONE