class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = ans = 1
        while j < len(nums):
            if nums[j] > nums[i]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1 
                ans += 1
            j+=1
        return ans
        
