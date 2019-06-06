p=int(input())
a=p//2
b=0
for x in range(2,a+1):
        if(p%x==0):
                b=1
if b==0:
        print("yes")
else:
        print("no")
