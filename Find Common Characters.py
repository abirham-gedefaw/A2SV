from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Start with first word's counter
        common_counter = Counter(words[0])
        
        # Intersect with counters of other words
        for word in words[1:]:
            common_counter &= Counter(word)
        
        # Convert counter to list
        result = []
        for char, count in common_counter.items():
            result.extend([char] * count)
        
        return result
            
        
