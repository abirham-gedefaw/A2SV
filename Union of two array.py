class Solution:    
    def findUnion(self, a, b):
        
        return sorted(set(a) | set(b))
