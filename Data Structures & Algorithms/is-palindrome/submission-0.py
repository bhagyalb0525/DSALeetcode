class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=""
        for i in s:
            if i.isalnum():
                res=res+i
                
        l=0
        r=len(res)-1
        while l<r:
            if res[l]!=res[r]:
                return False
            else:
                l+=1
                r-=1
        return True