def ext_euc(a, b):
    
    a, b=max(a,b),min(a,b)
    x1,y1,x2,y2=1,0,0,1
    
    while not(a%b==0):
        floor=a//b
        
        x1=x1-floor*y1
        temp1=x1
        x1,y1=y1,temp1

        x2=x2-floor*y2
        temp2=x2
        x2,y2=y2,temp2

        a,b=b,a%b
    return temp1, temp2

print(ext_euc(45,35))
    
