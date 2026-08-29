class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s, b, l, d = "", "", [], {}
        for i in word:
            if i.isalpha():
                s += " "
            elif i.isdigit():
                s += i
        for i in s:
            if i != " ":
                b += i
            elif i == " ":
                if b != "":
                    l.append (int(b))
                    b = ""
        if len(word) == 1 and word.isalpha():
            return 0
        elif b != "":
            l.append (int(b))
        for i in range (0, len(l)):
            if l[i] in d:
                d [l[i]] += 1
            else:
                d [l[i]] = 1
        return len (d)