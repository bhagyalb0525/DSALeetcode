class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        count=0
        maxcount=0
        for num in seen:
            if num-1 not in seen:
                count=1
                while num+1 in seen:
                    count+=1
                    num+=1
                maxcount=max(maxcount,count)
        return maxcount