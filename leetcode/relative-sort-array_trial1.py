class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        maxi = max(arr1)
        count = [0] * (maxi+1)
        for num in arr1:
            count[num] += 1
        
        target = 0
        for num in arr2: 
            while count[num] > 0: 
                arr1[target] = num
                target += 1
                count[num] -= 1
            
        for num in range(len(count)):
            while count[num] > 0:
                arr1[target] = num
                target += 1
                count[num] -= 1
        
        return(arr1)
        