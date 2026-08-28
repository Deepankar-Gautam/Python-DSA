class Solution:
    def numberOfSteps(self, num: int) -> int:
        x = num
        s = 0
        while x != 0:
            if x % 2 == 0:
                x //= 2
                s += 1
            else:
                x -= 1
                s += 1 
        return s