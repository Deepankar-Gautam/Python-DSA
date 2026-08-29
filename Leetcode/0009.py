class Solution:
    def isPalindrome(self, x: int) -> bool:
        d = x
        n = 0
        if d < 0:
            return False
        while d != 0:
            l = d % 10
            n = n * 10 + l
            d = d // 10
        return x == n