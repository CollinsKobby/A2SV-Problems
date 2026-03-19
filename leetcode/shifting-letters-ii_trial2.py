class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n+1)
        shift_count = 0
        result = []

        for l, r, k in shifts:
            if k == 1:
                diff[l] += 1
                diff[r+1] -= 1
            else:
                diff[l] -= 1
                diff[r+1] += 1
        
        for i in range(n):
            shift_count += diff[i]

            original_char = ord(s[i]) - ord('a')
            shifted_char = (original_char + shift_count) % 26 
            result.append(chr(shifted_char + ord('a')))

        return ''.join(result)

                