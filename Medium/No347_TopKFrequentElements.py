class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range (len(nums) + 1)]
        
        for key, v in count.items():
            freq[v].append(key)
            
        res = []    
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
        