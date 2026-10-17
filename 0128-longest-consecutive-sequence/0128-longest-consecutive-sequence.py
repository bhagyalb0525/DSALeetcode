class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=sorted(nums)
        count=1
        maxcount=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            elif nums[i+1]-nums[i]>1:
                count=1
            maxcount=max(maxcount,count)
        return maxcount if nums else 0

