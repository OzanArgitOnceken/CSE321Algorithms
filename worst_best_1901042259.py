def merge(arr,left,mid,right):
    h1=mid-left+1
    h2=right-mid
    
    leftArr=[0]*h1#creating the left array
    rightArr=[0]*h2#creating the right array
    for i in range (0,h1):
        leftArr[i]=arr[left+i]#putting variables
    for i in range (0,h2):
        rightArr[i]=arr[mid+i+1]#putting variables
    i = 0
    j = 0
    k = left 
    while i<h1 and j<h2:
        if leftArr[i]>rightArr[j]:#if the right one bigger puts right array's values to array before left 
            arr[k]=rightArr[j]
            j+=1
        else:
            arr[k]=leftArr[i]
            i+=1
        k+=1
    while i<h1:
        arr[k]=leftArr[i]
        i+=1
        k+=1
    while j<h2:
        arr[k]=rightArr[j]
        j+=1
        k+=1
    
def mergeSort(arr,left,right):#divides array 2 parts and sends parts to merge sort
    if left<right:
        mid=(left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)
def worstBest(arr):#for easier calling from main
    n = len(arr)
    mergeSort(arr, 0, n-1)
    
    print("Worst result: ",arr[0])
    print("Best result: ",arr[n-1])
arr = [12, 11, 13, 5, 6, 7,8]
worstBest(arr)