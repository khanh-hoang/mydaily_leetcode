#Time :O(n)
#Space:O(n)
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mydict = {k: v for k,v in knowledge}
        cur = ""
        going = False
        res = []
        for c in s:
            if c == "(":
                going = True
            elif c == ")":
                going = False
                res.append(mydict.get(cur, "?"))
                cur = ""
            elif going:
                cur += c
            else:
                res.append(c)
        return "".join(res)