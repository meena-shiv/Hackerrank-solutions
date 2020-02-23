a,b=map(int,input().split())
l=sorted([int(i) for i in input().split()])
ant=0
i=0
while(1):
    k=l[i]
    for j in range(i,a):
        if l[j]-k<=b:
            i+=1
        else:
            break
    ant+=1
    k=l[i-1]
    for j in range(i,a):
        if l[j]-k<=b:
            i+=1
        else:
            break
    if i>=len(l):
        break
print(ant)
