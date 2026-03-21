import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0: return False

        a, b = 0, int(math.sqrt(c))
        while a <= b:
            curr_sum = (a*a) + (b*b)
            if curr_sum == c:
                return True
            elif curr_sum < c:
                a += 1
            else:
                b -= 1
        
        return False