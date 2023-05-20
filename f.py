x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=int(input("enter the value of y"))

def maximum(x,y,z):
    if (x >= y) and (x >= z):
      return x
    elif (y >= x) and (y >= z):
       return y
    else:
       return z
maximum() 