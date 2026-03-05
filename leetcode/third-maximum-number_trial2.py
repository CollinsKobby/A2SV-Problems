class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = sorted(set(nums), reverse=True)
        return unique[2] if len(unique) >= 3 else unique[0]
        