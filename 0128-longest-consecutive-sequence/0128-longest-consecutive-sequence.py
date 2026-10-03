class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen=set(nums)
        maxcount=0
        curr=0
        count=0
        for num in seen:
            if num-1 not in seen:
                count=1
                curr=num
            while curr+1 in seen:
                count+=1
                curr+=1
            maxcount=max(maxcount,count)
        return maxcount
            

