class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        nn = n
        while nn >= 3:
            nn = nn/3
        if nn == 1:
            return True
