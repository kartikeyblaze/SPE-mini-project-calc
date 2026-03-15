import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        raise ValueError("Cannot take factorial of negative number")
    return math.factorial(a)

def natural_log(a):
    if a <= 0:
        raise ValueError("Natural log only defined for positive numbers")
    return math.log(a)

def power(a, b):
    return math.pow(a, b)

def main():
    while True:
        print("\n--- Scientific Calculator ---")
        print("1.  Addition (+)")
        print("2.  Subtraction (-)")
        print("3.  Multiplication (*)")
        print("4.  Division (/)")
        print("5.  Square Root (sqrt)")
        print("6.  Factorial (fact)")
        print("7.  Natural Log (ln)")
        print("8.  Power (pow)")
        print("9.  Exit")
        
        try:
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice == '9' or choice.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break
            
            if choice in ['1', '2', '3', '4', '8']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1': print(f"Result: {add(num1, num2)}")
                elif choice == '2': print(f"Result: {subtract(num1, num2)}")
                elif choice == '3': print(f"Result: {multiply(num1, num2)}")
                elif choice == '4': print(f"Result: {divide(num1, num2)}")
                elif choice == '8': print(f"Result: {power(num1, num2)}")
            
            elif choice in ['5', '6', '7']:
                num = float(input("Enter number: "))
                if choice == '5': print(f"Result: {square_root(num)}")
                elif choice == '6': print(f"Result: {factorial(int(num))}")
                elif choice == '7': print(f"Result: {natural_log(num)}")
            
            else:
                print("Invalid choice! Please select 1-9.")
        except ValueError as e:
            print(f"Input Error: Please enter valid numbers. ({e})")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
