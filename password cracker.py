for i in range(int(input())):
    p=0
    f=int(input())
    a=input().split(' ')
    b=input()
    v=0
    s1=''
    s2=''
    for k in range(len(b)):
        c=b[v:k+1:1]
        if c in a:
            s1+=c
            s2+=c+' '
            v=k+1
    if len(s1)==len(b):
        print(s2)
    else:
        print('WRONG PASSWORD')

                
                
