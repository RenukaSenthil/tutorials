string=input()
newstr=''
for i in string:
    newstr=i+newstr
if(newstr==string):
    print("yes")
else:
    print("no")
