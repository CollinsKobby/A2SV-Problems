class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum, last_sum = 0, 0
        l = 0
        sett = set()

        for r in range(len(nums)):
            while nums[r] in sett or len(sett) == k:
                sett.remove(nums[l])
                last_sum -= nums[l]
                l += 1
            last_sum += nums[r]
            sett.add(nums[r])
            if len(sett) == k:
                max_sum = max(max_sum, last_sum)
        
        return max_sum
