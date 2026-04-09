class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, table = [], {}

        for c in nums2:
            while stack and stack[-1] < c:
                table[stack.pop()] = c
            stack.append(c)
        
        return [table[a] if a in table else -1 for a in nums1]