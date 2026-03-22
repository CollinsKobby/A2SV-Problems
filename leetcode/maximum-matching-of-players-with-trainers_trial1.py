class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l, r, count = 0, 0, 0

        while r < len(trainers) and l < len(players):
            if players[l] <= trainers[r]:
                l += 1
                r += 1
                count += 1
            else:
                r += 1
        
        return count