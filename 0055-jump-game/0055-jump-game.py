class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i=0
        farthest=0
        for i in range(len(nums)-1):
            if i>farthest:
                return False
            farthest=max(farthest,i+nums[i])
        return farthest>=len(nums)-1
