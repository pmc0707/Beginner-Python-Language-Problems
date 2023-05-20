a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
if(a==b==c):
    print("This is right triangle")
elif (a==b!=c):
    print("this is isoscelus triangle")
else:
    print("this is scalane triangle")