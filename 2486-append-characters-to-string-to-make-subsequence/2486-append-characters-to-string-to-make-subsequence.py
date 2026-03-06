class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        second = 0
        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                second += 1
            first += 1
        return len(t) - second


               


        