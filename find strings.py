l1=[]
for i in range(int(input())):
    a=input()
    for j in range(len(a)):
        for k in range(j+1,len(a)+1):
            l1.append(a[j:k])        
p=set(l1)
p=list(p)
p.sort()
for d in range(int(input())):
    x=int(input())
    if x>len(p):
        print('INVALID')
    else:
        print(str(p[x-1]))
