'''a = 'softwarica'
for i in a:
    print(i)

a = 'softwarica'
for i in range(len(a)):
    print(a[i])

a = 'softwarica'
n = len(a)
for i in range(n):
    print(a, '=',a[i])
    '''

#1
a = [1, 2, 3, 4]

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')

#2. Write a python program to reverse a string using forloop. 
a="python"
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")

#3. Write a python program to print a multiplication table of any number using for loop. 
num=int(input("Enter a number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#4. 4.Write a program to print each item in a list of fruits: ["apple", "banana", "cherry"].
fruits=["apple","banana","cherry"]
for i in fruits:
    print(i)

#5.Write a program to print the following using forloopa. first 10 even numbersb.first 10 odd numbers
for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
print()
for i in range(1,21):
    if i%2!=0:
        print(i,end=" ")
print()

#6.Write for loop statement to print the following series:10 20 30 --------300
for i in range(1,31):
    print(i*10,end=" ")
print()

#7.7. Write a forloop statement to print the following series:105 98 -------7
for i in range(105,6,-7):
    print(i,end=" ")
print()

#8. Write a program to print the factorial of a number accepted from user.

a = int(input("Enter a number"))
factorial = 1
for i in range(1,num+1):
    factorial *= i
    print(f"The Fctorial of {num} is {factorial}")

#9. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.

num = int(input("Enter an integer: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"The reversed number is {reversed_num}")

#10. Write a python program that return the number of characters in a string. myList = "Parameter"
myList = "Parameter"
count = 0
for i in myList:
    count += 1
print(count)

#11. Write a Python program to multiply all the numbers in a list using for loop. Sample list = [8, 2, 3, -1, 7]
sample_list = [8, 2, 3, -1, 7]
result = 1

for num in sample_list:
    result *= num

print(f"The result of multiplying all the numbers in the list is {result}")

#12.
#12. Write a Python program to sum all the numbers in a list using for loop.
# Sample list: [8, 2, 3, 0, 7]
sample_list = [8, 2, 3, 0, 7]
total = 0
for num in sample_list:
    total += num
print(f"Sum of all numbers: {total}")

#13. Accept a string from the user and display only those characters which are present at an even index.
user_string = input("Enter a string: ")
even_index_chars = user_string[::2]
print(f"Characters at even indices: {even_index_chars}")

#14. Accept a string from the user and display only those characters which are present at an odd index.
user_string = input("Enter a string: ")
odd_index_chars = user_string[1::2]
print(f"Characters at odd indices: {odd_index_chars}")

#15. Write a program to sum numbers from 1 to 10 (or any number) using a for loop.
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of numbers from 1 to 10: {total}")

#16. Write a Python program to print the even numbers from a given list.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [num for num in sample_list if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

#17. Write a Python program to print the odd numbers from a given list.
# Sample List: [12, 13, 14, 15, 16, 17, 18, 19]
sample_list = [12, 13, 14, 15, 16, 17, 18, 19]
odd_numbers = [num for num in sample_list if num % 2 != 0]
print(f"Odd numbers: {odd_numbers}")

#18. Write a program to print numbers from 1 to 100 that are divisible by 5.
for num in range(1, 101):
    if num % 5 == 0:
        print(num, end=" ")
print()

#19. Write a program to find the largest number in a list.
# Sample List: [3, 7, 2, 8, 5]
numbers = [3, 7, 2, 8, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number: {largest}")

#20. Write a program to print the square of numbers from 1 to 10.
for i in range(1, 11):
    print(f"Square of {i}: {i**2}")

#21. Write a program to print the cube of numbers from 1 to 5.
for i in range(1, 6):
    print(f"Cube of {i}: {i**3}")

#22. Write a program to print each character in the string "Python" using a for loop.
string = "Python"
for char in string:
    print(char)

#23. Write a program to print all numbers between 1 and 50 that are divisible by both 3 and 5.
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
print()

                     #DONE

  









