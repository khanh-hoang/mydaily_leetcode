class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mymap = {}
        for k, v in enumerate(order):
            mymap[v] = k
            
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if mymap[words[i][j]] > mymap[words[i+1][j]]:
                        return False
                    break
        return True 