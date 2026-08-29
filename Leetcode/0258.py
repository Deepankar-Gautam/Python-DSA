class Solution:
    def addDigits(self, num: int) -> int:
        x = num
        while True:
            if x < 10:
                return x
            else:
                b = 0
                while x != 0:
                    l = x % 10
                    x = x // 10
                    b = b + l
                x = b