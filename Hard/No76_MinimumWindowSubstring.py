class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) == 0 or len(s) == 0:
            return ""
        
        mymap = Counter(t)
        count = len(t)
        window = ""
        start = 0 
        
        for i in range(len(s)):
            if mymap[s[i]] > 0:
                count -=1
            mymap[s[i]] -= 1
            
            while count == 0:
                lenwin = i - start + 1
                if not window or lenwin < len(window):
                    window = s[start:i+1]
                
                mymap[s[start]] += 1
                if mymap[s[start]] > 0:
                    count += 1
                start+=1
        
        return window 