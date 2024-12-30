#1.
for i in range(1, 11):
    print("SOFTWARICA")

#2.
a = [1, 2, 3]
sum = 0
for i in a:
    sum = sum + i
print(sum)

#3.
a = [1, 'a', 2, 4, 'c']
a = str(a)
for i in a:
    if i.isalpha():
        print(i)

#4.
a = [4, 5, 2, 3]
mul = 1
for i in a:
    mul = mul * i
print(mul)

#5.
a = [4, 5, 2, 3]
mul = 1
for i in a:
    mul *= i
print(mul)

#6.
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#7.
a = [1, 2, 3, 4]
reversed_list = a[::-1]
print(reversed_list)

#8.
a = [1, 2, 3, 4]
new_list = [i + 1 for i in a]
print(new_list)

#9.
a = [1, 2, 3, 4]
print(a[0], a[-1])

#10.
a = [1, 2, 3, 4]
print(a[0], a[1], a[-1])

#11.
a = [1, 2, 3, 4]
a[1] = "a"
del a[2]
print(a)

#12.
a = [1, 2, 3, 4, 5]
odds = [i for i in a if i % 2 != 0]
evens = [i for i in a if i % 2 == 0]
print(f"Odds: {odds}, Evens: {evens}")

#13.
a = [1, 2, 3, "d", 4, 5, "a"]
integers = [i for i in a if isinstance(i, int)]
strings = [i for i in a if isinstance(i, str)]
print(f"Integers: {integers}, Strings: {strings}")

#14.
a = [1, 2, 3, 4, "a", "b"]
integers = []
strings = []
for item in a:
    if isinstance(item, int):
        integers.append(type(item))
    elif isinstance(item, str):
        strings.append(type(item))
print(f"Integer types: {integers}, String types: {strings}")

#15.
user_input = input("Enter a string: ")
digits = sum(c.isdigit() for c in user_input)
letters = sum(c.isalpha() for c in user_input)
spaces = sum(c.isspace() for c in user_input)
print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")

#16.
username = input("Enter username: ")
password = input("Enter password: ")
if username and password:
    print("Valid username and password")
else:
    print("Invalid input")

#17.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#18.
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}")

#19.
for num in range(1, 9):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#20.
a = [1, 2, 3, 4]
print(a[0], a[1])

#21.
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
odd_sum = sum(i for i in range(start, end + 1) if i % 2 != 0)
print(f"Sum of odd numbers: {odd_sum}")

#22.
even_sum = sum(i for i in range(1, 101) if i % 2 == 0)
print(f"Sum of even numbers: {even_sum}")

#23.
string = input("Enter a string: ")
spaces = string.count(' ')
print(f"Number of spaces: {spaces}")

#24.
a = [1, 2, 3, 4]
cubes = [i ** 3 for i in a]
print(cubes)

#25.
a = "programming"
reversed_string = a[::-1]
print(reversed_string)

#26.
for i in range(50):
    if i > 7:
        break
    print(i)

#27.
string = "Python"
for char in string:
    print(char)

#28.
a = ["ram", "shyam", 1, 2]
for name in a:
    print(f"Hello!, {name}")

#29.
a = ["ram", "shyam", 1, 2]
dr_list = [f"Dr.{item}" for item in a]
print(dr_list)

#30.
a = [1, 2, 3, 4]
squares = [i ** 2 for i in a]
print(squares)

#31.
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
positives = [i for i in lst1 if i > 0]
print(positives)

#32.
for i in range(7):
    if i not in [3, 6]:
        print(i)

#33.
a = [1, "a", True]
b = [type(item) for item in a]
print(b)

#34.
for i in range(5):
    print(i)
else:
    print("Done")

#35.
for i in range(105, 97, -7):
    print(i)

#36.
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
for char in bad_chars:
    string = string.replace(char, "")
print(string.replace(" ", ""))

#37.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = len([i for i in nums if i % 2 == 0])
odd_count = len([i for i in nums if i % 2 != 0])
print(f"Even: {even_count}, Odd: {odd_count}")

#38.
sum_multiples = sum(i for i in range(3, 100) if i % 3 == 0 or i % 5 == 0)
print(f"Sum of multiples: {sum_multiples}")

#39.
even_sum = sum(i for i in range(1, 101) if i % 2 == 0)
odd_sum = sum(i for i in range(1, 101) if i % 2 != 0)
print(f"Even sum: {even_sum}, Odd sum: {odd_sum}")

#40.
number = int(input("Enter a number: "))
if str(number) == str(number)[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#41.
number = int(input("Enter a number: "))
num_digits = len(str(number))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))
if sum_of_powers == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#42.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowels = "".join(char for char in string if char not in vowels)
print(no_vowels)

#43.
number = int(input("Enter a number: "))
divisors = [i for i in range(1, number) if number % i == 0]
if sum(divisors) == number:
    print("Perfect number")
else:
    print("Not a perfect number")

#44.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = [i for i in list1 if i in list2]
print(f"Common elements: {common}")

#45.
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
                           #DONE



