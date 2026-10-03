class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        for i in freq:
            if freq[i]>=2:
                return i 