class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum, currSum = 0, 0
        l, r = 0, 0
        sett = set()

        for r in range(len(nums)):
            while nums[r] in sett:
                sett.remove(nums[l])
                currSum -= nums[l]
                l += 1

            sett.add(nums[r])
            currSum += nums[r]

            maxSum = max(maxSum, currSum)
            print(currSum)
        
        return maxSum