class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        
        res = [0] * n
        x = 2*k + 1
        l = 0
        for i in range(n):
            if i < k or n - (i+1) < k:
                res[i] += -1
            else:
                if l == 0:
                    avg = nums[i+k] // x
                else:
                    avg =  (nums[i+k] - nums[l-1]) // x
                l += 1
                res[i] += avg
        
        return res
                

