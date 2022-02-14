class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = i = 0
        while i < len(nums):
            if sum(nums[i+1:]) == left:
                return i
            left += nums[i]
            i += 1
        return -1