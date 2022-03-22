#Time :O(m + n)
#Space:O(m + n)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalStr = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph]) 
        words = normalStr.split()
        banned = set(banned)
        mymap = defaultdict(int)
        for word in words:
            if word not in banned:
                mymap[word] += 1
        return max(mymap.items(), key = lambda x: x[1])[0]
