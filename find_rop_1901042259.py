def countReverses(inp):#it makes easier calling function from main
    return divide(inp,0,(len(inp)-1)) 
def divide(inp,left,right):#this function divides input
    if left>right or left==right:
        return 0
    mid=(left+right)//2
    leftinv=divide(inp,left,mid)#for hold the inversions of left
    rightinv=divide(inp,mid+1,right)#for hold the inversions of right
    return leftinv + rightinv + conquerAndCount(inp, left, mid, right)#total inversion
def conquerAndCount(inp, left, mid, right):
    i=left
    inv=0
    while i<=mid:#comparing left with right
        k=mid+1
        while k<=right:
            if inp[i]>inp[k]:
                inv+=1
                print("(",inp[i],",",inp[k],")")
            k+=1
        i+=1
    return inv
inp=[4,3,2,5,6,1,-5]
print("There are",countReverses(inp),"reverse-ordered pairs.")