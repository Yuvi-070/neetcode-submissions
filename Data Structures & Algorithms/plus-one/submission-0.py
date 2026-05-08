class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        m = 1
        k = []
        for i in range(len(digits) - 1, -1, -1):
            res += digits[i] * m
            m *= 10
        res += 1
        while res > 0:
            k.insert(0, res % 10)
            res //= 10
        return k
