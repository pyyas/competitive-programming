class Solution:
    def fib(self, n: int) -> int:
        ans = []
        for i in range(n+1):
            if i == 0:
                ans.append(0)
            elif i == 1:
                ans.append(1)
            else:
                ans.append(ans[i-2]+ans[i-1])
        return ans[-1]
