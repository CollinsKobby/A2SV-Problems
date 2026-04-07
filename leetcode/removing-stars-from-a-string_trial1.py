class Solution:
    def removeStars(self, s: str) -> str:
        non_star = []

        for char in s:
            if char != "*":
                non_star.append(char)  
            else:
                if non_star:
                    non_star.pop()
        
        return "".join(non_star)
