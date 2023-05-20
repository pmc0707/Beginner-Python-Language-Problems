h=float(input("enter the hypotaneous"))
b=float(input("enter the base"))
p=float(input("enter the perpendicualar"))
h=(b**2+p**2)**(1/2)
print(h)
if(h**2==p**2+b**2):
    print("this is right triangle")
else:
    print("this is not right triangle")    
