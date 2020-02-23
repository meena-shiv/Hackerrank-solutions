def subsets(s):
    if len(s) == 0:
	    return [[]]
	    
    h, t = s[0], s[1:]
    
    p = subsets(t)
    
    q = [([h] + ss) for ss in p]
    
    return p + q
 
print(subsets(input()))
