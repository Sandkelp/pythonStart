num1 = input("Enter a number: ")
op = input("Enter an operator: ")
num2 = input("Enter another number: ")

if op == '+':
    result = float(num1) + float(num2)

elif op == '-':
    result = float(num1) - float(num2)

elif op == '*':
    result = float(num1) * float(num2)

elif op == '/':
    result = float(num1) / float(num2)

elif op == '%':
    result = float(num1) % float(num2)

print(result)

