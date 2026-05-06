class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        k=0
        for n in num:
            if (n-1) not in num:
                l = 0
                while (n+l) in num:
                    l+=1
                k=max(l,k)
        return k


            

    
