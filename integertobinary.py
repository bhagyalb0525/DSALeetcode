n=int(input())
binarr=[]
while n>1:
    binarr.append(n%2)
    n=n//2
binarr.append(n)
for i in range(len(binarr)-1,-1,-1):
    print(binarr[i],end="")

#binary to integer
p=len(binarr)-1
num=0
for i in range(len(binarr)-1,-1,-1):
    num+=(binarr[i]*(2**p))
    p-=1
print()
print(num)