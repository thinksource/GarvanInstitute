size=int(input())
str_arr = input().split(' ')
Arr=[int(num) for num in str_arr]

def myprint(arr):
    ps=""
    for i in arr:
       ps+=str(i)+" "
    print(ps[:-1])

def insertionSort(arr):
    size=len(arr)
    p=arr[size-1]
    for i in range(size-2, -2,-1):
        if arr[i]>p and i>=0:
            arr[i+1]=arr[i]
        else:
            arr[i+1]=p
        myprint(arr)
        if arr[i]<=p:
            break

insertionSort(Arr)
