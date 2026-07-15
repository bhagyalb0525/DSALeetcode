class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            dict1[nums[i]]=dict1.get(nums[i],0)+1
        items=list(dict1.items())
        items.sort(key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(items[i][0])
        return result

