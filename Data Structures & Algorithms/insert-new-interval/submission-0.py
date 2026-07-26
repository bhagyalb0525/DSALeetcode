class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=result[-1][1]:
                result[-1][1]=max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
        intervals=result
        return intervals