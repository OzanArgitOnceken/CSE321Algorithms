def subCounter(str,start,end):
    sum=0;
    size=len(str)
    for i in range(0,size):
        if str[i]==start:
            for j in range(i+1,size):
                    if str[j]==end:
                            sum=sum+1
    return sum

print("There are "+str(subCounter("XTXZXXJZWX",'X','Z'))+" substrings")