class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        x=list(freq.items())
        l=sorted(x,key=lambda k:k[1],reverse=True)
        res=""
        for i,j in l:
            res+=i*j
        return res