class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sumarr=0
        maxsum=nums[0]
        for num in nums:
            sumarr+=num
            maxsum=max(maxsum,sumarr)
            if sumarr<0:
                sumarr=0
        return maxsum
