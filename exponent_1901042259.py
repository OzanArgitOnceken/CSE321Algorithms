def bruteExponentional(a,n):
    result=1#result is 1 for first multiplying
    i=0
    while i<n:#a*a for  n times
        result*=a
        i+=1
    return result
def divideExponentional(a,n):
    result=1#result is 1 for first multiplying
    if n==1:#if there is no another dividing n return a for multiply
        return a
    else:
        if n%2==1:#if I did not check it is odd or even it sends 3 like 1 and 1 in here it sends it 1 and 2
            result*=divideExponentional(a,(n//2))
            result*=divideExponentional(a,((n//2)+1))
        else:#divide it 2 if it is even and make result the multiply of other halves
            result*=divideExponentional(a,(n//2))
            result*=divideExponentional(a,(n//2))
    return result

print(bruteExponentional(2,4))
print(divideExponentional(11,2))