class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        res = k

        if k == len(blocks):
            if blocks.count('B') == k:
                return 0
            else:
                return min(res, blocks.count('W'))

        for r in range(k, len(blocks)+1):
            if blocks[l:r].count('B') != k:
                res = min(res, blocks[l:r].count('W'))
            else:
                return 0
            l += 1
        
        return res


        