import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.sort()
l=len(arr)
size=l
print(l)
i=0
while i<l:
    j=1
    if j+i>=l:
        break
    while arr[i]==arr[j+i]:
        j+=1
    size-=j
    i+=j
    print(size)
