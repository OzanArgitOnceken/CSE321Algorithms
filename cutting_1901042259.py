def cutter(a):
    sum=0;
    if a<=1:      #if a can not divide anything else return 0
        return 0;
    else:
        sum=sum+cutter(a/2); #sum of cutting equals other cutting; #if second half is odd add 1 and send for cut for correct return
        return sum+1;
print(cutter(100));