class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strings:
            key = []
            for i in range(len(s)-1):
                dif = 26 + ord(s[i+1]) - ord(s[i])
                key.append(str(dif%26))
            k = ",".join(key)
            res[k].append(s)
        print(res)
        return res.values()