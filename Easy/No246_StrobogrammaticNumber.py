#Time: O(n)
#Space:O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num) - 1
        while l<=r:
            if num[l] == num[r]:
                if num[l] == "0" or num[l] == "8" or num[l] == "1":
                    l+=1   
                    r-=1
                else:
                    return False
            else:
                if (num[l] == "6" and num[r] == "9") or (num[l] == "9" and num[r] == "6"):
                    l+=1
                    r-=1
                else:
                    return False
        return True 
            