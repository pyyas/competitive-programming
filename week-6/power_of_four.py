class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        nn = n
        while nn >= 4:
            nn = nn/4
        if nn == 1:
            return True
