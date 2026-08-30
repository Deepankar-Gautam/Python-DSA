class Solution:
    def minimumSum(self, num: int) -> int:
        x, n1, n2, l = str (num), "", "", []
        for i in x:
            l.append (i)
        l.sort()
        for i in range (0, len(l) - 1, 2):
            n1 = n1 + str (l[i])
            n2 = n2 + str (l[i+1])
        y = int(n1) + int (n2)
        return y