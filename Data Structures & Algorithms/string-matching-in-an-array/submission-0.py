class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i , substring in enumerate(words):
            is_sub = False
            for j, string in enumerate(words):
                if i!=j and substring in string:
                    is_sub = True
                    break
            if is_sub:
                res.append(substring)
        return res