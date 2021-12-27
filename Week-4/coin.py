class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = piles[(len(piles)//3):]
        sum1= 0
        for x in range(len(mine)-2, -1, -2):
            sum1 += mine[x]
        return sum1