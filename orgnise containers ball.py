
for i in range(int(input())):
    l1,l2,s1,p=[],[],{},0
    for j in range(int(input())):
        s=[int(k) for k in input().split(' ')]
        for l in range(len(s)):
            if p==0:
                s1[l]=s[l]
            else:
                s1[l]+=s[l]       
        p+=1
        l1.append(sum(s))
    l2,f=[g for g in s1.values()],0
    for h in l1:
        if h not in l2:
            print('Impossible')
            f=1
            break
    if f==0: print('Possible')

       


