class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = [0] * len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(len(nums)):
                if nums[j] < curr:
                    new[i] += 1
        return new
