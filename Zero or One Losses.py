class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loss_count = Counter()
        
        # First pass: Count losses and ensure all players are recorded
        for winner, loser in matches:
            # This ensures winners with 0 losses are in the Counter
            loss_count[winner] += 0
            loss_count[loser] += 1
        
        # Initialize result lists
        zero_loss = []
        one_loss = []
        
        # Categorize players (sorted iteration for final order)
        for player in sorted(loss_count.keys()):
            if loss_count[player] == 0:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        
        return [zero_loss, one_loss]
