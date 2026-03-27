class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        def flip(k):
            arr[:k+1] = arr[:k+1][::-1]
        
        for i in range(len(arr)-1, 0, -1):
            for j in range(1, i+1):
                if arr[j] == i+1:
                    flip(j)
                    result.append(j+1)
                    break
            flip(i)
            result.append(i+1)
        
        return result