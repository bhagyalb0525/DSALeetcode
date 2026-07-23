class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        conseq=0
        count=0
        for i in num_set:
            if i-1 not in num_set:
                current=i
                count=1
                while current+1 in num_set:
                    count+=1
                    current+=1
                conseq=max(conseq,count)
        return conseq