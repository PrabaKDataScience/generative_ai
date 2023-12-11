import sys

print("Enter the first number: ")
num1 = float(input())

print("Enter the second number: ")
num2 = float(input())

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("Enter your choice (1-4): ")
choice = int(input())

result = 0

if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        sys.exit(1)
else:
    print("Invalid choice!")
    sys.exit(1)

print("Result: ", result)