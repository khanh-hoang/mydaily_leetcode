#Time : O(n)
#Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                print(prefix)
                if len(prefix) == 0:
                    return ""
        return prefix