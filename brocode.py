while True:
    try:
        NumberSquared = input("What number would you like to square? ")
        NumberSquared = int(NumberSquared)
        if NumberSquared <= 0:
            print("You entered 0 or a negative number, please enter a number greater than 0")
        else:
            print("The square of", NumberSquared, "is", NumberSquared**2)
            break
    except ValueError:
        print("Invalid input, please enter a valid number")
