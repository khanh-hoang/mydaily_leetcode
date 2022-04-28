#Time :O(n+m) n: length arr, m: range arr
#Space:O(n+m)
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minA = min(arr)
        maxA = max(arr)
        shift = -minA
        new_arr = [0] * (maxA - minA + 1)
        answer = []
        
        for num in arr:
            new_arr[num+shift] = 1
            
        min_dif = maxA - minA
        pre = 0
        
        for cur in range(1, maxA + shift + 1):
            if new_arr[cur] == 0:
                continue
            if cur - pre == min_dif:
                answer.append([pre - shift, cur - shift])
            elif cur - pre < min_dif:
                answer = [[pre - shift, cur - shift]]
                min_dif = cur - pre
            pre = cur
        
        return answer
                
        """
        Time: O(nlogn)
        Space:O(n)
        arr.sort()
        temp = float("inf")
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] <= temp:
                temp = arr[i+1] - arr[i]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == temp:
                res.append([arr[i], arr[i+1]])
        return res
        """