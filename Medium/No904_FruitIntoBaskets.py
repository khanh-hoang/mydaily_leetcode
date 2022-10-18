class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits or len(fruits) == 0:
            return 0
        res = 0 
        left = right = 0
        counter = Counter()
        
        while right < len(fruits):
            counter[fruits[right]] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    counter.pop(fruits[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res