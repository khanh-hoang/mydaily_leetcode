#Time: O(n)
#Space:O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ourlist =[]
        for i in range(1, n+1):
            if i%3 == 0 and i%5 ==0:
                ourlist.append("FizzBuzz")
            elif i%3 == 0:
                ourlist.append("Fizz")
            elif i%5 == 0:
                ourlist.append("Buzz")
            else:
                ourlist.append(str(i))
                
        return ourlist