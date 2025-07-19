num1 = float(input("Enter the first Digit: "))
num2 = float(input("Enter the second Digit: "))

# Show operation choices
operations = {
    '1':'+',
    '2':'-',
    '3':'*',
    '4':'/'
    }
# Get operation choice from user
choice = input("Enter your choice (1Add/2Sub/3Mul/4Div): ")

# Perform the chosen operation
if choice == '1':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
