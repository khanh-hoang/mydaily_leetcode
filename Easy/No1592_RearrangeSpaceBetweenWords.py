#Time: O(n)
#Space:O(1)
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split() 
        spaces = text.count(" ")
        if len(words) == 1:
            return words[0] + spaces * " "
        
        fixed_spaces = spaces // (len(words) - 1)
        extra_spaces = spaces % (len(words) - 1)
        
        res = ""
        for word in words[:-1]:
            res += word + fixed_spaces * " "
        res += words[-1] 
        res += extra_spaces * " "
        return res