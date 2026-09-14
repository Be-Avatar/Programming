class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        s = nums
        for i in range(len(nums) - 1, -1, -1):
            s.append(nums[i])
        return s