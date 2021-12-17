class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        x = [int(elem) for elem in nums]
        x.sort()
        maximum = str(x[len(x)-k])
        return maximum
