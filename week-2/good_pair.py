class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair_count = 0
        for i in range(len(nums)):
            j = i
            while j<(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pair_count += 1
                j += 1
        return good_pair_count
