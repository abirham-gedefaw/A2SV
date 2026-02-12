class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        flag = True
        for ghost in ghosts:
            my_distance = (abs(0 - target[0]) + abs(0 - target[1]) )
            ghost_distance = (abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]))
            if ghost_distance <= my_distance:
                flag = False
        return flag
