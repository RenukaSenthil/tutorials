n=int(input())
s=list(map(int,input().split()))
l=[]
if(sorted(set(s))==sorted(s)):
    print("unique")
else:
    for i in s:
        if s.count(i)>1:
            l.append(i)
    print(*(set(sorted(l))))
