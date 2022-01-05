class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if str(nums[j]) + str(nums[i]) > str(nums[i]) + str(nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
        return str(int(''.join(map(str, nums))))
