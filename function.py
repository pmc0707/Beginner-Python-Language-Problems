# def name(x,y):
#     return x,y
# print(name(3,5,6,8))
def name(a):
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    return c==2
ls=[]
for k in range(1,1001):
    ls.append(k)
    
ls=list(filter(name,ls))
print(ls,len(ls))