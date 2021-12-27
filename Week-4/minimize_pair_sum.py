class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        arr = []
        for i in range(len(nums)//2):
            arr.append((nums[i] + nums[(len(nums)-1)-i]))
        ans = max(arr)
        return ans