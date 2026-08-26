digit = int (input ("Enter you digit : "))
num = digit
print ("Last digits")
while num != 0:
    last = num % 10
    num = num // 10
    print (last)
print (f"Your number : {digit}")