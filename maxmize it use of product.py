from itertools import product
k,m=map(int,input().split(' '))
l,l1=[],[]
for i in range(k):
    l.append([int(p) for p in input().split()][1:])
print(l)
for j in product(*l):
    x=0
    for r in j:
        x+=r**2
    l1.append(x%m)
print(max(l1))
    
    
    
    
