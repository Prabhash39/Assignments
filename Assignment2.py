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


