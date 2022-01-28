#Time :O(n)
#Space:O(1)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ptr1 = ptr2 = -1
        res = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                ptr1 = i
                if ptr2 != -1:
                    res = min(res, ptr1 - ptr2)
            if wordsDict[i] == word2:
                ptr2 = i
                if ptr1 != -1:
                    res = min(res, ptr2 - ptr1)
        return res