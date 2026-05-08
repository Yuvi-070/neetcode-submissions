class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i=k%len(nums)
        nums[:]=nums[-i:]+nums[:-i]
        """
        Do not return anything, modify nums in-place instead.
        """
        