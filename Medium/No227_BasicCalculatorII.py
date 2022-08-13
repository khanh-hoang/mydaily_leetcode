class Solution:
    def calculate(self, s: str) -> int:
        s += "+0"
        oper = "+"
        curnum = 0
        lastnum = 0
        res = 0
        for i in range(len(s)):
            if s[i].isdigit():
                curnum = curnum * 10 + int(s[i])
            elif s[i] != " ":
                if oper == "+":
                    res += lastnum
                    lastnum = curnum
                elif oper == "-":
                    res += lastnum
                    lastnum = -curnum
                elif oper == "*":
                    lastnum *= curnum
                elif oper == "/":
                    lastnum = int(lastnum/curnum)
                oper, curnum = s[i], 0
        res += lastnum
        return res
                