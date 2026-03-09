class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i, j = 0, 0
        size = len(arr)
        while i < size:
            if arr[i] == 0:
                j = i+1
                i += 2
                arr.insert(j, 0)
                arr.pop()
            else:
                i += 1