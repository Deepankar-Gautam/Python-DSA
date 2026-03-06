"""
===============================================
      Data Structures and Algorithms
===============================================


Data Structure: is a way of organising, storing, and managing data in memory so it can be accessed and modified efficiently.

Software: is a set of executable instructions that process input, manipulate data, and produce output.

Software (contain programs) = Program (becomes process while execution) = Process

note: "Process" word only applicable for the programs running in memory.

"""

#=========================================================
# Extration of last digit 
#=========================================================

n = int (input ("Enter your number : "))
num = n

def last_digit(num):
    while num != 0:
        l = num % 10     # give last digit
        num = num // 10  # remove last digit from number
        print (l) 

last_digit(n)
print (n)

#=========================================================
# Reverse a digit
#=========================================================

n = int (input ("Enter a number : "))
b = 0

while n != 0:
    l = n % 10      # give last digit
    n //= 10        # remove last digit
    b = b*10 + l    # shift value to left and add the last digit  # result = (result * 10) + initial_number

print (b)