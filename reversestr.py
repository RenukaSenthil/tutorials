s=input()
ns=[]
for i in s:
    if i not in ns:
        ns.append(i)
print(*(sorted(ns[::-1])),sep="")
