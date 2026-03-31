class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        count = 0
        s1 = ""
        s2 = ""

        while l < r:
            if s[l] != s[r]:
                s1 = s[:r] + s[r+1:]
                s2 = s[:l] + s[l+1:]
                break
            l += 1
            r -= 1
        print(s1)
        print(s2)
        if s1 == s1[::-1] or s2 == s2[::-1]:
            return True
        else:
            return False