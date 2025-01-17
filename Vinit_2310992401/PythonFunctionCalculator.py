import math

def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2

def subtraction(num1, num2):
    return num1 - num2


def exponent(num1, num2):
    return num1 ** num2

def square_root(num):
    if num < 0:
        return "Error: Cannot calculate square root of a negative number"
    else:
        return math.sqrt(num)

def square(num):
    return math.pow(num, 2)

def factorial(num):
    if num < 0:
        return "Error: Cannot calculate factorial of a negative number"
    else:
        return math.factorial(int(num))

print("Calculator to perform operations:")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Square Root")
print("7. Square")
print("8. Factorial")

operation = int(input("Enter the operation number (1/2/3/4/5/6/7/8): "))

if operation in [1, 2, 3, 4, 5]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
else:
    num = float(input("Enter the number: "))

if operation == 1:
    result = addition(num1, num2)
    print("Addition of the two numbers is:", result)
elif operation == 2:
    result = subtraction(num1, num2)
    print("Subtraction of the two numbers is:", result)
elif operation == 3:
    result = multiplication(num1, num2)
    print("Multiplication of the two numbers is:", result)
elif operation == 4:
    result = division(num1, num2)
    print("Division of the two numbers is:", result)
elif operation == 5:
    result = exponent(num1, num2)
    print("Exponentiation of the two numbers is:", result)
elif operation == 6:
    result = square_root(num)
    print("Square root of the number is:", result)
elif operation == 7:
    result = square(num)
    print("Square of the number is:", result)
elif operation == 8:
    result = factorial(num)
    print("Factorial of the number is:", result)
else:
    print("Invalid operation number. Please select from 1 to 8.")
