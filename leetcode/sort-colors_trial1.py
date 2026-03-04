class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        maxi = max(nums)
        count = [0] * (maxi+1)

        for num in nums:
            count[num] += 1

        target = 0
        for index,value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1

        return(nums)
        