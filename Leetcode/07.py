class Solution:
    def reverse(self, x: int) -> int: 
        digit = x
        num = 0
        status = True
        if x < 0:
                digit = digit * (-1)
                status = False
        while digit > 0:
            last = digit % 10
            digit = digit // 10
            num = num * 10 + last
        if status == False:
            num = num * (-1)
        
        if (num > 2 ** (31) - 1) or (num < (-1)*(2) ** (31)):
            return 0

        return num