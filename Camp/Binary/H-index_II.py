class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)
        while l < r:
            m = (l+r)//2
            if citations[m]>=(len(citations)-m):
                r = m
            else:
                l = m+1
        return (len(citations)-l)
