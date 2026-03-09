class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] < target and i < j:
                    count += 1
        
        return count