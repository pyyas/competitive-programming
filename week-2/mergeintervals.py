class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        
        for j in range(len(intervals)):
            i = 1
            while i < len(intervals):

                if intervals[i-1][1] >= intervals[i][0] and intervals[i-1][1] < intervals[i][1]:
                    intervals[i-1][1] = intervals[i][1]
                    intervals.pop(i)

                elif intervals[i-1][1] >= intervals[i][0] and intervals[i-1][1] >= intervals[i][1]:
                    intervals[i-1] = intervals[i-1]
                    intervals.pop(i)
                elif intervals[i-1][0] == intervals[i][0] and intervals[i][1] == intervals[i+1][1]:
                    intervals[i-1] = intervals[i-1]
                    intervals.pop(i)
                i +=1

        return intervals
