class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_count = {}
        result = []

        for ball, new_color in queries:
            if ball in ball_color:
                old_color = ball_color[ball]

                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            ball_color[ball] = new_color
            color_count[new_color] = color_count.get(new_color, 0) + 1
            result.append(len(color_count))
        
        return result

        

        
        
