a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

if a > b:
    a, b = b, a

    number = a

while number <= b:
 print(number)
number += 1