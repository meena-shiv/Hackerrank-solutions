l1=[]
x=int(input())
for i in range(x):
    l1.append(input().split(' '))
l2=sorted(l1,key=lambda x: x[2])
for i in l2:
    print(''.join('Mr'' '+i[0]+' '+i[1] if i[3]=='M' else 'Ms'+' '+i[0]+' '+i[1]))


        
    

