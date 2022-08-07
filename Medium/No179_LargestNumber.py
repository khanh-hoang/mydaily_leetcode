class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def largest(x, y):
            if x+y > y+x:
                return -1
            elif x+y < x+y:
                return 1
            else:
                return 0
        
        output ="".join(sorted(map(str, nums), key=cmp_to_key(lambda a,b : largest(a,b))))
        
        return "0" if output[0] == "0" else output