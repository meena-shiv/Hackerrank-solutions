for i in range(int(input())):
    a,b=map(int,input().split())
    l=[int(i) for i in input().split()]
    l1=[]
    p=1000000
    for i in range(a-b+1):
        if sum(l[i:i+b])<p:
            q=i
            p=sum(l[i:i+b])
    print(q+1,q+b)
        
