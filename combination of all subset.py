def powerSet(string , index , curr,L): 
      
    if index == len(string): 
        L.append(curr)

         
    powerSet(string, index + 1, curr +str( string[index]),L) 
    powerSet(string, index + 1, curr,L)
    return L
      
  
s1 =[int(i) for i in input().split()]
index = 0
curr = ""
L=[]
p=powerSet(s1, index , curr,L)
print(p)
