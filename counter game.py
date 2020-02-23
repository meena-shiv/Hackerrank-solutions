#mine
'''for i in range(int(input())):
    l=[2**j for j in range(65)]
    n=int(input())
    y=0
    while(1):
        if n in l:
            n=n//2
            y+=1
        else:
            t=n
            while(n not in l):
                n-=1    
            n=t-n
            y+=1
        if n==1:
            break
    if n%2!=0:
        print('Richard')
    else:
        print('Louise')'''


players = "Richard", "Louise"
T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    x=bin(N-1)
    p=x.count('1')
    if p%2==0:
        print('Richard')
    else:
        print('Louise')
    
