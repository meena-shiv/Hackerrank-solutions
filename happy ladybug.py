for i in range(int(input())):
    k=int(input())
    p=input()
    l,q,x=[],0,0
    for i in p:
        if i!="_":
            l.append(i)
    if "_" in p:
        l.sort()
    if len(l)==1:
        print("NO")
        x=1
    else:
        for i in range(len(l)):
            if i==0:
                if l[i]!=l[i+1]:
                    print("NO")
                    x=1
            elif i==len(l)-1:
                if l[i]!=l[i-1]:
                    print("NO")
                    x=1
            else:
                if l[i]!=l[i+1] and l[i]!=l[i-1]:
                    x=1
                    print("NO")
            if x==1:
                break
    if x==0:
        print("YES")
