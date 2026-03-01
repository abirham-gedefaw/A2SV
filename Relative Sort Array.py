class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = Counter(arr1)
        result = []

        for num in arr2:
            result.extend([num]* count[num])
            del count[num]
        for num in sorted(count.keys()):
            result.extend([num] * count[num])
        return result
