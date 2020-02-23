a=input()
s,l=list(set(a)),[]
s.sort()
for i in s:
    l.append(a.count(i))
l1,d=sorted(l,reverse=True),0
for i in l1:
    if d==3:
        break
    p=l.index(i)
    print(s[p],i)
    l.remove(i)
    s.remove(s[p])
    d+=1
