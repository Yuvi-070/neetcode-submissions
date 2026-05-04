class Solution:
    def scoreOfString(self, s: str) -> int:
        score=0
        for t in  range(len(s)-1):
            score+=abs(ord(s[t]) - ord(s[t+1]))
        return score



        