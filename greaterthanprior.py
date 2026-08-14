arr=[7,4,8,2,9,2,3,10,11]
count=1
maximum=arr[0]
for i in range(1,len(arr)):
    if arr[i]>maximum:
        count+=1
        maximum=arr[i]
print(count)