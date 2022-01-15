class Solution:
    def myPow(self, x: float, n: int) -> float:
        poww = n
        ans = 1
        if poww<0:
            poww= -poww
            x = 1/x
        while poww > 0:
            if poww%2==1:
                ans = ans*x
                poww = poww-1
            elif poww%2==0:
                x = x*x
                poww = poww//2
        return ans
