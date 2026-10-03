class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        for i in nums:
            if i not in hash:
                hash[i]=1
            else:
                hash[i]+=1
        L=list(hash.items())
        L.sort(key=lambda x:x[1],reverse=True)
        return L[0][0]
