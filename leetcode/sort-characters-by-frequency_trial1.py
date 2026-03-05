class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter

        c = Counter(s)
        c_sort = sorted(c, key=c.get, reverse=True)

        ans = []

        for char in c_sort:
            ans.append(char * c[char])
        
        return "".join(ans)


        