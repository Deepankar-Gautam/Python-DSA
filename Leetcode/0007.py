class Solution:
    def reverse(self, x: int) -> int: 
        d = x
        n = 0
        s = True
        if x < 0:
                d = d * -1
                s = False
        while d > 0:
            l = d % 10
            d = d // 10
            n = n * 10 + l
        if s == False:
            n = n * -1     
        if n > 2 ** 31 - 1 or n < -1*2 ** 31:
            return 0
        return n