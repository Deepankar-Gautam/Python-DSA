#method 1 : normal
number = int (input ("Enter your number : "))
num = number
count = 0

while num != 0:
    last = num % 10
    num = num // 10
    count += 1

print (f"Your number {number} contains {count} digits")

#method 2 : with log
from math import *
print (f"Your number {number} contains {int (log10(number) + 1)} digits")