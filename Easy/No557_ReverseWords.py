#Time: O(n)
#Space:O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)
    
    """
    mylist = s.split(" ")
        res = "" 
        for word in mylist:
            word = word[::-1]
            res += word + " "
        return res[:-1]
    """