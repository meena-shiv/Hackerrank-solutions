for i in range(int(input())):
    l1=[j for j in input()]
    l2=[j for j in input()]
    s=''
    while(1):
        if len(l1)==0 or len(l2)==0:
            break
        if l1[0]<l2[0]:
            s+=l1[0]
            l1.remove(l1[0])        
        elif l1[0]==l2[0]:
            s+=l1[0]
            l1.remove(l1[0])   
        else:
            s+=l2[0]
            l2.remove(l2[0])  
    if len(l2)==0:
        for k in l1:
            s+=k
    else:
        for q in l2:
            s+=q
    print(s)
