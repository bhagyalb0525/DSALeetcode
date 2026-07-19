class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        answer=0
        maxfreq=0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            maxfreq=max(maxfreq,freq[s[right]])
            while (right-left+1)-maxfreq>k:
                freq[s[left]]-=1
                left+=1
            answer=max(answer,right-left+1)
        return answer