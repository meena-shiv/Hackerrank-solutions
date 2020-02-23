a,b=map(int,input().split())
p=input()
y=a//2
s=''
for i in range(y):
    s+='9'
v=0
if a==1 and b==1:
        print('9')
        v=1
        s=0
for j in range(int(s),0,-1):
    d=str(j)
    if a%2==0:
        q=d+d[ : :-1]
        r=0
        for k in range(len(q)):
            if p[k]!=q[k]:
                r+=1
        if r<=b:
            print(q)
            v=1
            break
        if len(q)<len(p):
            break
    else:
        for j in range(9,int(p[a//2])-1,-1):
            q=d+str(j)+d[ : :-1]
            r=0
            for k in range(len(q)):
                if p[k]!=q[k]:
                    r+=1
            if r<=b:
                print(q)
                v=1
                break
            if len(q)<len(p):
                break
    if v==1:
        break
if v==0:
    print('-1')
        
