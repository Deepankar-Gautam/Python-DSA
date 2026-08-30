class Solution:
    def isFascinating(self, n: int) -> bool:
        n1 = n * 2
        n2 = n * 3
        x = str(n) + str(n1) + str(n2)
        for i in range (0, len(x) - 1):
            for j in range ((i+1), len(x)):
                if x[i] == x[j] or x[j] == "0":
                    return False
        return True