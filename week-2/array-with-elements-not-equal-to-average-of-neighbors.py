import random
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums) - 1:
            if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                i = 1
                random.shuffle(nums)
            else:
                i += 1
        return nums    
