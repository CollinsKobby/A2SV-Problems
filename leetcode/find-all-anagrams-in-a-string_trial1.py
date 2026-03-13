from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size, l = len(p), 0
        pcount = Counter(p)
        scount = Counter(s[:size])
        output = []

        if pcount == scount:
            output.append(0)

        for r in range(size, len(s)):
            scount[s[r]] += 1
            scount[s[l]] -= 1
            if scount[s[l]] == 0:
                del scount[s[l]]
            l += 1
            if pcount == scount:
                output.append(l)
        return output

