class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def sumtotal(n):
            total=0
            while n!=0:
                digit=n%10
                total+=pow(digit,2)
                n=n//10
            return total
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n=sumtotal(n)
        return True