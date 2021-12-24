class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter(nums)
        for i in count:
            if i == (k - i):
                ans += (count[i]//2)
            elif (k - i) in count:
                ans += min(count[i], count[k - i])
                count[i] = 0
        return ans
