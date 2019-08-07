n=int(input())
Sum=0
rev=0
while(n> 0):
    r=n%10
    Sum=Sum+r
    n=n//10
Temp=Sum
while(Sum>0):
    a=Sum%10
    rev=(rev*10)+a
    Sum=Sum//10
if(rev==Temp):
    print("Yes")
else:
    print("No")
