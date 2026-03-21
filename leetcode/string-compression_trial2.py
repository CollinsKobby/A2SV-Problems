class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j, n = 0, 0, len(chars)

        while i < n:
            char = chars[i]
            count = 0
            while i < n and chars[i] == char:
                i += 1
                count += 1
            chars[j] = char
            j += 1

            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1

        return j