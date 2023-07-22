import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    print("Simple Scientific Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")

    while True:
        choice = input("Enter operation number (or 'q' to quit): ")

        if choice.lower() == 'q':
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '6':
            num1 = float(input("Enter the number: "))
            print("Result:", square_root(num1))
        elif choice == '7':
            num1 = float(input("Enter the number: "))
            base = float(input("Enter the base (default is 10): "))
            print("Result:", logarithm(num1, base))
        elif choice == '8':
            angle = float(input("Enter the angle in degrees: "))
            print("Result:", sin(angle))
        elif choice == '9':
            angle = float(input("Enter the angle in degrees: "))
            print("Result:", cos(angle))
        elif choice == '10':
            angle = float(input("Enter the angle in degrees: "))
            print("Result:", tan(angle))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()