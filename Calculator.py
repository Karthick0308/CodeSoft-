def calculator():
    while True:
        # Prompt the user to input two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue
        
        # Prompt the user to choose an operation
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the number of the operation you want to perform: ")

        # Perform the calculation based on the chosen operation
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}\n")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}\n")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}\n")
        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}\n")
        else:
            print("Invalid operation choice. Please choose a valid operation.\n")
            continue
        
        # Prompt the user to decide whether to continue or exit
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
    