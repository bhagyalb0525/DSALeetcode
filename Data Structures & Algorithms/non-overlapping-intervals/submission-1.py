class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        previous=intervals[0]
        remove=0
        for i in range(1,len(intervals)):
            if intervals[i][0]<previous[1]:
                remove+=1
                if previous[1]>intervals[i][1]:
                    previous=intervals[i]
            else:
                previous=intervals[i]
        return remove