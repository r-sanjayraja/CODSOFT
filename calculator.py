def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)
    
    print(f'{num1} {operation} {num2} = {result}')

if __name__ == "__main__":
    main()
