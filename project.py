a=int(input("enter the starting point"))
b=int(input("enter the stopping point"))
c=int(input("enter the jump point"))
d=int(input("enter  1 for increment number"'\n'" enter 2 for decrement"'\n'"emter 3 for horizontalincrement"'\n'"eenter 4 forhorizontaly decrement"'\n'"enter the number"))
verticalincrement=1
verticaldecrement=2
horizontalincrement=3
horizontaldecrement=4
if(1==d):
    print("number is in increment")
    for i in range(a,b+1,c):
        print(i)
elif(2==d):
    print("Number  is in decrement")
    for k in range(b,a-1,-c):
        print(k)
elif(3==d):
    print("Number  is in horizontaly incerment")
    for j in range(a,b+1,c):
        print(j,end=" ")
elif(4==d):
    print("Number in horizontaly decrement")
    for l in range(b,a-1,-c):
        print(l,end=" ")
else:
    print('invalid syntax')        
                