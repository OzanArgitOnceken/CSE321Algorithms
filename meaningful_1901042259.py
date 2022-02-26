def partition(arr,low,hi):
    pivot=arr[hi]
    i=low-1
    for j in range(low,hi):
        if arr[j]<pivot:
            i+=1
            swap(arr,j,i)
    swap(arr,i+1,hi)
    return (i+1)
def swap(arr,a,b):
    t=arr[a]
    arr[a]=arr[b]
    arr[b]=t
def largest(a,k):
    return kthSmallest(a, 0, len(a)-1,(len(a)- k)+1)
def kthLargest(a,l,r,k):
    if (k > 0 and k <= r - l + 1):
        index=partition(a,l,r)
        if index==k:
            return a[index]
        elif index<k:
            return kthLargest(a,index+1,r,k)
        return kthLargest(a,l,index-1,k)
    print("Out of bound")
    return -1
arr = [ 9,5,1,56,41,87,52,3,10 ]
print("K-th largest element=",largest(arr, 3))