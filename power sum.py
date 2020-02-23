'''from itertools import combinations
x=int(input())
y=int(input())
k=int(x**(1/y))
l=[]
for j in range(1,k+1):
    l.append(j)   
c=0
for i in range(1,k+1):
    p=combinations(l,i)
    for j in p:
        g=0
        for v in j:
            g+=v**y
        if g==x:
            c+=1
print(c)'''
def powersum(X,P,N=1):
    i_pow = pow(N,P)
    if i_pow > X:
        return 0
    elif i_pow == X:
        return 1
    return powersum(X,P,N+1) + powersum(X-i_pow,P,N+1)
x=int(input())
p=int(input())
print(powersum(x,p))
            
            
