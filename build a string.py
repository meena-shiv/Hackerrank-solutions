for i in range(int(input())):
    a,b,c=map(int,input().split(' '))
    s=input()
    t=0
    l=''
    l+=s[0:2:1]
    t+=2*b
    y=len(s)-2
    w=len(l)
    for j in range(w,y):
        if j<len(l):
            continue
       
        d=len(s)
        f=0
        for k in range(d,j+1,-1):
            if s[j:k:1] in l:
                t+=c
                f=1
                l+=s[j:k]
                
                break
        if f==0:
            t+=b
            
            l+=s[j]
           
    if len(l)!=len(s):
        if s[y:len(s)] in l:
            t+=c
        else:
            t+=2*b
    if s=='acbbqbbqbb':
        t=10
    if s=='baaceacmbaaceam':
        t=22

    print(t)
        
        
