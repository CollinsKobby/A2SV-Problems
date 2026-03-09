class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while j < n and i < m+n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                nums1.pop()
        
        for q in range(len(nums2[j:])):
            nums1.pop()
        nums1.extend(nums2[j:])
        
        return nums1

        