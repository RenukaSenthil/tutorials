length=int(input())
l=list(str(input()))
vowel=['a','A','e','E','i','I','O','o','U','u']
for i in l:
    if i in vowel:
        l.remove(i)
print("".join(l)[::-1])
