# Factorial calculator using recursion

def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return x * factorial(x-1)

def factorial_input():
    try:
        # User can input a value
        n = int(input("Enter your value: "))
        result = factorial(n)

        # Displaying the result
        print('The Factorial of', n, 'is', result)

    except ValueError:
        print("Enter a valid integer.")

# Naming it
factorial_input()
