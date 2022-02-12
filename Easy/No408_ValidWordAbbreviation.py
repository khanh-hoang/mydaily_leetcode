#Time: O(n)
#Space:O(1)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i, j = 0, 0
        
        while i<m and j<n:
            if word[i] == abbr[j]:
                i+=1
                j+=1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k+=1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == m and j == n