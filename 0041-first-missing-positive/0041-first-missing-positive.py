class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)
        seen=[0 for _ in range(n+2)]
        for num in nums:
            if num>=1 and num<=n:
                seen[num]=1
        for i in range(1,n+1):
            if seen[i]==0:
                return i
        return n+1