class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        i=0
        j=0
        count=0
        players.sort()
        trainers.sort()
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count