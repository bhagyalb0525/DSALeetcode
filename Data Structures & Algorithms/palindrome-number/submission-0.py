class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal=0
        temp=x
        reverse=0
        while temp>0:
            digit=temp%10
            reverse=reverse*10+digit
            temp=temp//10
        if reverse==x:
            return True
        else:
            return False