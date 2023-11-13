class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        res = []
        
        for i in range(n):
            x = i + 1
            if x%5 == 0 and x%3 == 0:
                temp = "FizzBuzz"
            elif x%5 == 0:
                temp = "Buzz"
            elif x%3 == 0:
                temp = "Fizz"
            else:
                temp = str(x)
            
            res.append(temp)
        
        return res