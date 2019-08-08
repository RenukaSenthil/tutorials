s=input()
ns=[]
for i in s:
    if i not in ns:
        ns.append(i)
ns.sort()
print(*ns[::-1],sep="")
