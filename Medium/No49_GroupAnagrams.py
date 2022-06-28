class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list)
        result = []
        
        for i in strs:
            key = "".join(sorted(list(i)))
            mymap[key].append(i)
            
        for i in mymap.values():
            result.append(i)
        return result