def cutCandy(arr,n):
    maxVal=[0]*(len(arr)+1)
    for i in range(1,n+1):
        tempMin=-1#price can not be less than 0
        for j in range(i):
            if arr[j]+maxVal[i-j-1]>tempMin:
                tempMin=arr[j]+maxVal[i-j-1]
                maxVal[i]=arr[j]+maxVal[i-j-1]
    return maxVal[n]
print("Maximum Obtainable Value is " ,cutCandy([1, 5, 8, 9, 10, 17, 17, 20],8))
print("Maximum Obtainable Value is " ,cutCandy([25, 1, 1, 1, 11, 700, 17, 20],8))
print("Maximum Obtainable Value is " ,cutCandy([1, 5, 8, 9, 10, 17, 17, 20],8))