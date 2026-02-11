class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        result = []
        
        for j, s in enumerate(list2):
            if s in index_map:
                i = index_map[s]
                total = i + j
                if total < min_sum:
                    min_sum = total
                    result = [s]
                elif total == min_sum:
                    result.append(s)
        return result
