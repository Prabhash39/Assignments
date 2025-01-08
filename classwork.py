# floors = {'floor1', 'floor2', 'floor3'}
# rooms = {1, 2, 3}

# for i in floors:
#     for j in rooms:
#         if i == 'floor2':
#             if j == 1 or j == 3:
#                 continue
#             else:
#                 print(j)
#         elif i == 'floor3':
#             if j == 1 or j == 2:
#                 continue
#             else:
#                 print(j)
#         else:
#             print(j)



# # for row in range (6):
# #      for column in range(5):
# #          if (column == 0 or column == 4) and row !=0:
# #              print("*", end = " ")
# #          elif (column ==1 or column == 3 or column ==2) and (row == 0 or row ==3):
# #              print("*", end = " ")
# #          else:
# #              print(end = "  ")
# #      print()
   
# for row in range(7):
#     for column in range(500):
#         if column == 0:
#             print("*", end=" ")
#         elif column == 4 and (row == 1 or row == 2):
#             print("*", end=" ")
#         elif (row == 0 or row == 3) and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print() 
# for row in range(7):
#     for column in range(500):
#         if column == 0:
#             print("*", end=" ")
#         elif column == 4 and (row != 0 and row != 3):
#             print("*", end=" ")
#         elif (row == 0 or row == 3) and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print() 
# for row in range(700):
#     for column in range(5):
#         if (column == 0 or column == 4) and row != 0:
#             print("*", end=" ")
#         elif (row == 0 or row == 3) and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print()  
# for row in range(7):
#     for column in range(500):
#         if column == 0:
#             print("*", end=" ")
#         elif column == 4 and (row != 0 and row != 3 and row != 6):
#             print("*", end=" ")
#         elif (row == 0 or row == 3 or row == 6) and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print()
# for row in range(7):
#     for column in range(500):
#         if column == 0 or column == 4:
#             print("*", end=" ")
#         elif row == 3 and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print()
# for row in range(7):
#     for column in range(500):
#         if (column == 0 or column == 4) and row != 0:
#             print("*", end=" ")
#         elif (row == 0 or row == 3) and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print()  
# for row in range(7):
#     for column in range(500):
#         if (row == 0 or row == 3 or row == 6) and (column > 0 and column < 4):
#             print("*", end=" ")
#         elif column == 0 and (row == 1 or row == 2 or row == 6):
#             print("*", end=" ")
#         elif column == 4 and (row == 0 or row == 4 or row == 5):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()
# print()  
# for row in range(7):
#     for column in range(500):
#         if column == 0 or column == 4:
#             print("*", end=" ")
#         elif row == 3 and (column > 0 and column < 4):
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

# print()


# a = 'softwaricacollage'
# i = 0
# while i< len(a):
#     print(f'{a[i]}={i}')
#     i = i+1


# a = 'softwaricacollage'
# i = 0
# while i< len(a):
#     print(f"{a[i]}={i}")
#     i = i-1



# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     else:
#         print(i)
#     i = i +1

# correctusername = "12"
# correctpassword = "0"
# attempt = 3 
# while attempt > 0:
#     A = input("Enter Your username: ")
#     B = input("Enter Your password: ")

# if A == correctusername and B == correctpassword:
#     print("You have sucessfully Logged in")
#     break
# else:
#     attempt -= 1
#     print(f"Incorrect username or password. You have {attempt} attempts left.")
#     if attempt == 0:
#         print("You have been locked out due to too many failed attempts.")

import random
while True:
    a = input() 
    if a.lower() == 'exit':
        break
    try:
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        correct_answer = num1 * num2
        user_answer = int(input(f"What is {num1} * {num2}? "))
        if user_answer == correct_answer:
            print("Correct!")
else:
    print("Incorrect Answer, Please Try Again")
    

