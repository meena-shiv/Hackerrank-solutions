def powerSet(str1, index, curr,l): 
    n = len(str1) 
  
    if (index == n): 
        return 
  
    
    l.append(curr) 
  
    
    for i in range(index + 1, n): 
        curr += str1[i] 
        powerSet(str1, i, curr,l) 
  
        curr = curr.replace(curr[len(curr) - 1], "") 
  
    return l
  

str =input()
print(powerSet(str, -1, "",l=[])) 
