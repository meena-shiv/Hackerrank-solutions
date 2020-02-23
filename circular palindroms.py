a=int(input())
s=input()
for j in range(a):
    s1=s[j:a]+s[0:j]
    r=0
    for k in range(len(s1)):
        for n in range(k+1,a+1):
            p=s1[k:n]
            if p==p[: :-1]:
                t=len(p)
            if t>r:
                r=t
    print(r)
                    
