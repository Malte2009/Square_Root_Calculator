from decimal import getcontext, Decimal
from math import floor

number = input("Enter a number: ")

if not number.isdigit():
    print("Please enter a valid number")
    exit()

number = int(number)

decimalpoints = input("Enter the number of decimal points: ")

if not decimalpoints.isdigit() or int(decimalpoints) < 1:
    print("Please enter a valid number")
    exit()

getcontext().prec = int(decimalpoints)

percision = int(decimalpoints) * 3

i = 0
upperBound = number
lowerBound = 0

while i <= percision:
    middle = Decimal((upperBound + lowerBound) / 2)
    square = middle ** 2
    
    if square == number:
        print(f"The square root of {number} is {middle}")
        break
    elif square < number:
        lowerBound = middle
    else:
        upperBound = middle
    i += 1
    
    print(f"Progress: {i} / {percision}  |  {floor((100 / percision) * i)}%", end="\r")

print("")
print(f"The square root of {number} is {middle}")