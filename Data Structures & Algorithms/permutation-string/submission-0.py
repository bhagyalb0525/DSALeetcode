class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1={}
        for r in s1:
            if r not in freq1:
                freq1[r]=1
            else:
                freq1[r]+=1
        freq2={}
        left=0
        k=len(s1)
        for right in range(len(s2)):
            if s2[right] not in freq2:
                freq2[s2[right]]=1
            else:
                freq2[s2[right]]+=1
            if right-left+1 ==k:
                if freq1==freq2:
                    return True
                freq2[s2[left]]-=1
                if freq2[s2[left]]==0:
                    del freq2[s2[left]]
                left+=1
        return False