x=int(input())
y=int(input())
z=int(input())
n=int(input())
f=[]
ls=[]
for i in range(x+1): 
    for j in range(y+1): 
        for k in range(z+1): 
            print([i,j,k])
            if (i+j+k)!=n:
                f=[i,j,k]
                ls.append(f)
print(ls)