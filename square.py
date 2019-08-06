num=int(input())
sum=0
while(num>0):
    new=num%10
    sum=sum+new*new
    num=num//10
print(sum)
