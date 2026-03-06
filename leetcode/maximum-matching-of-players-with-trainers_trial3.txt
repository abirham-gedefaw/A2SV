class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        max_maching = 0
        first, second  = 0, 0
        while first < len(players) and second < len(trainers):
            while second < len(trainers) and players[first] > trainers[second]:
                second += 1
            if second < len(trainers):
                max_maching += 1
            first += 1
            second += 1
        return max_maching


        