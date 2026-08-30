class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        x = str(num)
        for i in range (0, len(x)):
            if num != 0 and num % int (x[i]) == 0:
                c += 1
        return c