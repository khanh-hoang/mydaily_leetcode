class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        n1 = len(num1)
        n2 = len(num2)
        res = [0] * (n1+n2)
        
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = int(num2[j]) * int(num1[i])
                posF = i+j 
                posB = i+j+1
                mul += res[posB]
                res[posB] = mul % 10
                res[posF] += mul // 10
        
        count = 0
        while count<len(res) and res[count] == 0:
            count +=1 
        
        return "".join(str(s) for s in res[count:])