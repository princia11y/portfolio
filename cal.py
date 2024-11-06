# Define a function for each arithmetic operation
def add(x, y):
    """Return the sum of two numbers"""
    return x + y

def subtract(x, y):
    """Return the difference of two numbers"""
    return x - y

def multiply(x, y):
    """Return the product of two numbers"""
    return x * y

def divide(x, y):
    """Return the quotient of two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Main program
def calculator():
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Prompt user to input operation choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Prompt user to input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation based on user's choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")

# Run the calculator program
calculator()