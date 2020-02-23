a=input()
b=input()
l=[]
for i in range(len(a)):
    s=''
    x=-1
    for j in range(i,len(a)):
        for k in range(len(b)):
            if a[j]==b[k] and k>x:
                s+=b[k]
                x=k
                break
    l.append(len(s))
print(max(l))

