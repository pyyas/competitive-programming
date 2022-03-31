class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            l, r = 0, n-1 
            while l<r:
                m = (l+r)//2
                if grid[i][m]>=0:
                    l = m+1
                else:
                    r = m
            if grid[i][l] < 0:
                ans += (n-l)
        return ans
