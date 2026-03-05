class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        arr = []

        for i in range(size):
            for j in range(size-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        for i in range(size):
            if nums[i] == target:
                arr.append(i)
        
        return(arr)

        