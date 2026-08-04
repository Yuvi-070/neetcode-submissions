class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=[]
        k=set()
        for nums in grid:
            for val in nums:
                if val not in k:
                    k.add(val)
                else:
                    n.append(val)
        m=len(grid)
        for i in range(1,m*m+1):
            if i not in k:
                n.append(i)
        return n

        
        