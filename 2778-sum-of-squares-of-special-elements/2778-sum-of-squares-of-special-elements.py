class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        squaresum=0
        n=len(nums)
        for i in range(1,len(nums)+1):
            if n%i==0:
                squaresum+=nums[i-1]*nums[i-1]
        return squaresum