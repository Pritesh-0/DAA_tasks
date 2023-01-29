#to find the number of anti-clock rotations done to an array after giving resultant array, initial array is sort

#approach 1: linear search; go through each element in brr to find smallest element and return its index. O(n)
def ls(n,arr,brr):
    key=arr[0]
    for i in range(n):
        if brr[i]==key:
            return i

#approach 2: binary search; binary search in arr(sorted) for the first element of brr, return n-(returned index). O(log n)
def bs(n,arr,brr):
    lo=0
    hi=n-1
    key=brr[0]
    while(hi-lo >1):
        mid=(hi+lo)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            hi=mid
        else:
            lo=mid+1


n=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))

print(ls(n,arr,brr))
print(n-bs(n,arr,brr))