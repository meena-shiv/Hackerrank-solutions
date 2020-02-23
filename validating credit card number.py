for i in range(int(input())):
    a,x,v,r,e,l1=input(),0,0,0,0,[]
    if len(a)==16:
        for k in a:
            if k.isdigit():
                x+=1
        if x==16 and  a[0] in '456':
            print('Valid')
        else:
            print('Invalid')
    else:
        for k in a:
            if k.isdigit():
                x+=1
                v+=1
                l1.append(k)
            if k=='-':
                if v!=4:
                    r=1
                v=0
        for q in range(len(l1)-4):
            if len(list(set(l1[q:q+4])))==1:
                e=1       
        if x==16 and a[0] in '456' and r==0 and ' ' not in a and '_' not in a and e==0:
            print('Valid')
        else:
            print('Invalid')
