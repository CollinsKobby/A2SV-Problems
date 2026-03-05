class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        size = len(score)
        answer = [""] * size

        pair = []
        for i in range(size):
            pair.append([score[i], i])

        for i in range(size):
            max_idx = i
            for j in range(i + 1, size):
                if pair[j][0] > pair[max_idx][0]:
                    max_idx = j
            
            pair[i], pair[max_idx] = pair[max_idx], pair[i]
            
            original_idx = pair[i][1]
            
            if i == 0:
                answer[original_idx] = "Gold Medal"
            elif i == 1:
                answer[original_idx] = "Silver Medal"
            elif i == 2:
                answer[original_idx] = "Bronze Medal"
            else:
                answer[original_idx] = str(i + 1)
        
        return(answer)
