class Solution:
    def reverseBits(self, n: int) -> int:
        binarr=[]
        while n>1:
            binarr.append(n%2)
            n=n//2
        binarr.append(n)
        while len(binarr)<32:
            binarr.append(0)
        pow=31
        num=0
        for i in range(len(binarr)):
            num+=binarr[i]*(2**pow)
            pow-=1
        return num