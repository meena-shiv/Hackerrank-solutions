for i in range(int(input())):
    a=input()
    b=input()
    l1=[]
    l2=[]
    for j in  range(len(a)):
        for k in range(j,len(a)):
            l1.append(a[j:k+1:1])
    for j in  range(len(b)):
        for k in range(j,len(b)):
            l2.append(b[j:k+1:1])
    l3=[]
    c=-1
    for g in l1:
        for h in l2:
            s=''.join(str(g)+str(h))
            if s==s[ : :-1]:
                if len(s)>c:
                    c=len(s)
                l3.append(s)
    l4=[]
    for n in l3:
        if len(n)==c:
            l4.append(n)
    l4.sort()
    if len(l4)==0:
        print('-1')
    else:
        print(l4[0]) 
