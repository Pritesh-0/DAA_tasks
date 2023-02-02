#implementation of Qsort

def qsort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x>pivot]
        return qsort(less)+[pivot]+qsort(greater)


arr=[6,4,3,8,10,1,2,5,7,9]
print(qsort(arr))