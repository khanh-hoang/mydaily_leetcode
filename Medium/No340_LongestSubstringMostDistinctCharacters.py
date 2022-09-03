class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if s == "":
            return 0
        storage = {}
        #"eceba" ; k = 2
        #a:4, b:3}
        #l = 3
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] in storage or (s[r] not in storage and k > len(storage)):
                storage[s[r]] = r
            elif s[r] not in storage and k == len(storage):
                l = min(storage.values())+1
                storage.pop(s[l-1])
                storage[s[r]] = r
            res = max(res, r-l+1)
            r+=1
            print(storage)
        return res
            