class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(left, right):
            while (left >=0 and right <len(s) and s[left]==s[right]):
                left-=1
                right +=1
            return s[left+1:right]
        
        result=""
        for i in range(len(s)):
            #odd case
            test = helper(i,i)
            if len(result) < len(test):
                result = test
            #even case
            test = helper(i,i+1)
            if len(result) < len(test):
                result = test
                
        return result