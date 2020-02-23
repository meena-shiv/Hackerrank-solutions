for p in range(int(input())):
    l=[]
    q,r=map(int,input().split(' '))
    for i in range(q):
        l.append(input())
    p=[]
    x,y=map(int,input().split(' '))       
    for k in range(x):
        p.append(input())
    k=0
    v=0
    s=0
    for i in p:
        for j in range(k,len(l)):
            if s==0:
                if i in l[j]:
                    k=j+1
                    v+=1
                    f=l[j].index(i)
                    s+=1
                    break
            else:
                if i in l[j] and f==l[j].index(i):
                    k=j+1
                    v+=1
                    f=l[j].index(i)
                    break
    if v==x:
        print('YES')
    else:
        print("NO")
            
