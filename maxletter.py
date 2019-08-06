s=str(input())
count=0
for i in s:
    freq=s.count(i)
    if freq>count:
        count=freq
        letter=i
print(letter)
