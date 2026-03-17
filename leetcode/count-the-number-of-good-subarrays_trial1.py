from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, good_subarrays, equal_pairs = 0, 0, 0, 0
        freq = defaultdict(int)

        while left < n:
            while right < n and equal_pairs < k:
                freq[nums[right]] += 1
                if freq[nums[right]] >= 2:
                    equal_pairs += freq[nums[right]] - 1
                right += 1
            
            if equal_pairs >= k:
                good_subarrays += n - right + 1

            freq[nums[left]] -= 1
            if freq[nums[left]] > 0:
                equal_pairs -= freq[nums[left]]
            left += 1

        return good_subarrays