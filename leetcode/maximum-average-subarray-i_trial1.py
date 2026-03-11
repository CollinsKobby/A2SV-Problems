class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum, last_sum = sum(nums[:k]), sum(nums[:k])
        n = len(nums)
        l, r = 0, k

        while r < n:
            curr_sum = last_sum - nums[l] + nums[r]
            max_sum = max(max_sum, curr_sum)
            last_sum = curr_sum

            l += 1
            r += 1
        
        return max_sum / k