from decimal import getcontext, Decimal
from math import floor
import time 

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

precision = int(decimalpoints) * 3

i = 0
upperBound = number
lowerBound = 0

start = time.time()

while i <= precision:
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
    
    print(f"Progress: {i} / {precision}  |  {floor((100 / precision) * i)}%", end="\r")

end = time.time()

print("")
print(f"Time taken: {round(end - start, 3)}s")
print(f"The square root of {number} is {middle}")