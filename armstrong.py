# a=int(input("enter the number"))
# sum=0
# for i in range(1,a):
#     r=a%i
#     if(r==0):
#        sum=int(sum)+i
# if(sum==a):
#     print("perfect")
# else:
#     print("not perfect")
        

a=int(input("enter the number"))
b=int(input("enter the number"))
fect=1
Fect=1
while(a>0):
    fect+=a
    Fect+=b
    a-=1
    b-=1
    print("fectorial",fect)
    print("fectorial",Fect)
    
