def lstSubStrings(s):
    if(len(s) is 0):
        return [s]
    substrs = []
    substrs.append(s)
    substrs.extend(lstSubStrings(s[1:]))
    substrs.extend(lstSubStrings(s[:-1]))
    substrs = list(set(substrs))
    return substrs
for i in range(int(input())):           
    a=input()
    b=int(input())
    k=lstSubStrings(a)
    k=list(set(k))
    k.sort()
    k=''.join(str(j) for j in k)
    print(k,k[b-1])
