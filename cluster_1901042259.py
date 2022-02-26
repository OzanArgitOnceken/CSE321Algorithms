def maxCluster(arr):
    current=arr[0]
    maxClust=current
    for i in range(1,len(arr)):
        current=max(arr[i],arr[i]+current)
        maxClust=max(maxClust,current)
    return maxClust
marmaray=[3,-5,2,11,-8,9,-5]
print(maxCluster(marmaray))