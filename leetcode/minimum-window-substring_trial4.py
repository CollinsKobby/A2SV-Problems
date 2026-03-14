class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if n > m:
            return("")
        
        from collections import Counter
        t_count = Counter(t)
        wind = Counter()
        need = len(t_count)
        have = 0
        l = 0
        ans, leng = [1,1], float('inf')

        for r in range(m):
            cur = s[r]
            wind[cur] += 1
            if cur in t_count and t_count[cur] == wind[cur]:
                have += 1
            while have == need:
                if leng > (r-l+1):
                    leng = r-l+1
                    ans = [l, r]
                wind[s[l]] -= 1
                if s[l] in t_count and t_count[s[l]] > wind[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        if leng != float('inf'):
            return s[l:r+1]
        return ""

        