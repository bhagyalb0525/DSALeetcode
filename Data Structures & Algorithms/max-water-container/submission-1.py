class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        maxarea=0
        while l<len(heights):
            for r in range(len(heights)):
                area=min(heights[l],heights[r])*(r-l)
                maxarea=max(maxarea,area)
            l+=1
        return maxarea
