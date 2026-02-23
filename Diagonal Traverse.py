class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        result = []
        for diagonal in range(rows + cols - 1):
            diag_elements = []

            start_row = 0 if diagonal < cols else diagonal - cols + 1
            start_col = diagonal if diagonal < cols else cols - 1

            current_row = start_row
            current_col = start_col

            while current_row < rows and current_col >= 0:
                diag_elements.append(mat[current_row][current_col])
                current_row += 1
                current_col -= 1

            if diagonal % 2 == 0:
                diag_elements = diag_elements[:: -1]

            result.extend(diag_elements)
        return result
                
                
            
