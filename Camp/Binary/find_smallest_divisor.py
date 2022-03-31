class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l<r:
            m = (l+r)//2
            if sum(math.ceil(x/m) for x in nums) > threshold:
                l = m + 1
            else:
                r = m
        return l
