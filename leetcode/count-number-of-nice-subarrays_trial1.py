class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd, l  = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd += 1
            
            while odd > k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
            
            if odd == k:
                temp = l
                while temp < r and nums[temp] % 2 == 0:
                    temp += 1
                    res += 1
                res += 1
            
        return res
