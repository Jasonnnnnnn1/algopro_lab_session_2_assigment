# Factorial calculator using recursion

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return x * factorial(x-1)

def factorial_user_input():
    try:
        # User can input a value
        n = int(input("Enter your value: "))

        # Displaying the result
        print(f"The factorial of {n} is {factorial(n)}.")

    except ValueError:
        print("Enter a valid integer.")


# Calling it
factorial_user_input()