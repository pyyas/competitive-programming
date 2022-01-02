class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        workon= sorted(count, key = count.get, reverse = True)
        sum1 = 0
        ans = 0
        for i in workon:
            sum1 += count[i]
            ans += 1
            if sum1 >= (len(arr)//2):
                return ans
