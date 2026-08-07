class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumarr=0
        for i in range(0,len(nums)+1):
            sumarr+=i
        miss=sumarr-sum(nums)
        return miss
        