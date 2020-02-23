k,x=map(int,input().split(' '))
l=sorted([int(y) for y in input().split(' ')])
l1=[0]*(k+1)
g=0
for i in l:
    for j in range(k+1):
        if j>=i:
                l1[j]+=l1[j-i]
        else:
            if g==0:
                l1[j]=1
        g+=1
print(max(l1))
