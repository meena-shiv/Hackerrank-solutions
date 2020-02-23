a=int(input())
l=[int(i) for i in input().split(' ')]
l1=[[0]*(a+1)for i in range(len(l))]
for i in range(len(l)):
    for j in range(0,a+1):
        if i==0:
            if l[i]==j:
                l1[i][j]=1
        else:
            if l[i]>j:
                l1[i][j]=l1[i-1][j]
            else:
                l1[i][j]=max(l1[i-1][j-l[i]],l1[i-1][j])
        l1[0][0]=1
    print(l1[i])
            
        
    
        
