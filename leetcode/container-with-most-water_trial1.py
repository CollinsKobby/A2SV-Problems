class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            wd = r - l
            hg = min(height[l], height[r])
            max_water = max(max_water, wd * hg)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water