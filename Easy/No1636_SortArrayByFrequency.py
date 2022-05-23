#Time: O(nlogn)
#Space:O(n)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key = lambda x: (count[x], -x))
        """
        res = []
        counter = Counter(nums)
        counter = sorted(counter.items(), key = lambda x: (x[1], -x[0]))
        print(counter)
        for k, v in counter:
            res += [k]*v
        return res
        """