class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=max(nums)
        points=[0]*(n+1)
        for num in nums:
            points[num]+=num
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=points[1]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],points[i]+dp[i-2])
        return dp[n]