class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) 
        st, en = -1, -1
        if nums == []:
            return -1, -1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid 
        if l < len(nums) and nums[l] == target: st = l
        l, r = 0, len(nums) 
        while l < r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid 
        if nums[r-1] == target: en = r - 1
        return st, en