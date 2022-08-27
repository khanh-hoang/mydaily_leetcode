class Solution:
    def bulbSwitch(self, n: int) -> int:
        """res = [1]*(n+1)
        for i in range(2, n+1):
            a = i
            while a < n+1:
                if res[a] == 1:
                    res[a] = 0 
                else:
                    res[a] = 1
                a += i
        print(res)
    #1 1 1 1 1
    #1 0 1 0 1
    #1 0 0 0 1
    #1 0 0 1 1 
    #1 0 0 1 0
    
    #1 1 1 1 1 1
    #1 0 1 0 1 0
    #1 0 0 0 1 1 
    #1 0 0 1 1 1 
    #1 0 0 1 0 1
    #1 0 0 1 0 0
    1 1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 0 1 0 1 0 1
    1 0 0 0 1 1 1 0 0 0 1
    1 0 0 1 1 1 1 1 0 0 1
    1 0 0 1 0 1 1 1 0 1 1
    1 0 0 1 0 0 1 1 0 1 1
    1 0 0 1 0 0 0 1 0 1 1
    1 0 0 1 0 0 0 0 0 1 1
    1 0 0 1 0 0 0 0 1 0 0
    1 0 0 1 0 0 0 0 1 0 0
    """
        if n == 0 :
            return 0
        else:
            return int(sqrt(n))
        