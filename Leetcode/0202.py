class Solution:
    def isHappy(self, n: int) -> bool:
        x = n
        b = 0
        y = {x : 1}
        if n == 1:
            return True
        else:
            while True:
                while x > 0:
                    l = x % 10
                    x = x // 10
                    b = b + l ** 2
                x = b
                b = 0
                if x == 1:
                    return True
                elif x in y:
                    y [x] += 1
                else:
                    y [x] = 1
                if y [x] > 1:
                    return False
