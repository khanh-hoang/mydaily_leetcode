#Time :O(n)
#Space:O(1)
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        p1 = p2 = p3 = 0
        while p1<len(arr1) and p2<len(arr2) and p3<len(arr3):
            if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1+=1
                p2+=1
                p3+=1
            else:
                if arr1[p1] < arr2[p2]:
                    p1+=1
                elif arr2[p2] < arr3[p3]:
                    p2+=1
                else: #it means arr1[p1] >= arr2[p2] >= arr3[p3]
                    p3+=1
        return res
        """
        This solution good about time but we do not use arrays are sorted
        counter = Counter(arr1+arr2+arr3)
        res = []
        for i in counter.keys():
            if counter[i] == 3:
                res.append(i)
        return res
        """