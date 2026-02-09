from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        
        for item in count_b:
            if count_b[item] > count_a[item]:
                return False
                
        return True
