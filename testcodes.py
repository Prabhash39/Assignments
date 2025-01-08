for row in range(7):
    for column in range(5):
        if column == 0:
            print("*", end=" ")
        elif column == 4 and (row == 1 or row == 2):
            print("*", end=" ")
        elif (row == 0 or row == 3) and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if column == 0:
            print("*", end=" ")
        elif column == 4 and (row != 0 and row != 3):
            print("*", end=" ")
        elif (row == 0 or row == 3) and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if (column == 0 or column == 4) and row != 0:
            print("*", end=" ")
        elif (row == 0 or row == 3) and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if column == 0:
            print("*", end=" ")
        elif column == 4 and (row != 0 and row != 3 and row != 6):
            print("*", end=" ")
        elif (row == 0 or row == 3 or row == 6) and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if column == 0 or column == 4:
            print("*", end=" ")
        elif row == 3 and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if (column == 0 or column == 4) and row != 0:
            print("*", end=" ")
        elif (row == 0 or row == 3) and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if (row == 0 or row == 3 or row == 6) and (column > 0 and column < 4):
            print("*", end=" ")
        elif column == 0 and (row == 1 or row == 2 or row == 6):
            print("*", end=" ")
        elif column == 4 and (row == 0 or row == 4 or row == 5):
            print("*", end=" ")
        else:
            print(end="  ")
    print(end="  ")  # Space between letters

    for column in range(5):
        if column == 0 or column == 4:
            print("*", end=" ")
        elif row == 3 and (column > 0 and column < 4):
            print("*", end=" ")
        else:
            print(end="  ")
    print()  # Move to the next line for the next row